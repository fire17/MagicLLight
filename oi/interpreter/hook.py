from rich import print as rprint
from .utils import merge_deltas, parse_partial_json


def xprint(*args,**kwargs):
    print("hooking")
    #print("###########",args,"############",kwargs)
    rprint(*args,**kwargs)



streams = []
calls = []
execs = []
done = [False]
state = {"streams":streams,"calls":calls,"execs":execs,"done":done}

from pprint import pprint 

'''Process Flow / state machine:
1. start_chat
2. chunk (s)
3. start_call (optional)
4. chunk (s)
5. finished_call
5. start_exec (missing)
6. chunk (lines)
7. start_chat
8. chunk (s)
5. finished_chat
'''

def export(event, final_payload=None, *args, **kwargs):
    return {"event":event,"payload":final_payload, "state": state}

def hook(data):
    chunk = data    
    finished =  chunk['choices'][0]['finish_reason']  # extract the message
    delta = chunk['choices'][0]['delta']  # extract the message
    fullChoice = chunk['choices'][0]
    if finished != None:
        if finished != "function_call":
            print("FFFFFFFFFFFF",finished)
            done[0] = True
            return export("finished_chat", {"reason":finished})
        else:
            return export("finished_call", {"reason":finished})
    else:
        found = False
        if "role" in delta:
            found = True
            done[0] = False
            streams.append("")
            return export("start_chat")#,{"role":payload["role"]})

        if "content" in delta:
            found = True
            streams[-1] += delta["content"]
            return export("chunk",{"data":delta["content"], "type":"content"})#,{"role":payload["role"]})
            
        print(":::::::::::::::::::::::")
        pprint(fullChoice)
        print(":::::::::::::::::::::::")
        
        if "function_call" in delta:
            if "name" in delta["function_call"]:
                found = True
                calls.append({"name":delta["function_call"]["name"], "arguments":"", "parsed_arguments":{}, "code":"", "language":""})
                return export("start_call",{"name":delta["function_call"]["name"], "type":"function_call"})#,{"role":payload["role"]})



            elif "arguments" in delta["function_call"]:
                if len(calls) == 0:
                    calls.append({"name":"function_call", "arguments":"", "parsed_arguments":{}, "code":"", "language":""})

                calls[-1]["arguments"] += delta["function_call"]["arguments"]
                arguments = calls[-1]["arguments"]
                new_parsed_arguments = parse_partial_json(arguments)
                if new_parsed_arguments:
                    # Only overwrite what we have if it's not None (which means it failed to parse)
                    calls[-1]["parsed_arguments"] = new_parsed_arguments

                #calls[-1]["arguments"] = payload["function_call"]["arguments"]
                if "parsed_arguments" in calls[-1]:
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    #alls[-1]["parsed_arguments"] = delta["function_call"]["parsed_arguments"]
                    if "code" in calls[-1]["parsed_arguments"]:
                        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!111111111111111code") 
                        code_delta = calls[-1]["parsed_arguments"]["code"][len(calls[-1]["code"]):]
                        calls[-1]["code"] += code_delta
                        return export("chunk",{"data":code_delta, "type":"function_call"})
                    if "language" in calls[-1]["parsed_arguments"]:
                        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!222222222222language") 
                        calls[-1]["language"] = calls[-1]["parsed_arguments"]["language"]
                        # Do this once if you do send something here
                        return export("chunk",{"data":f"", "type":"function_call"})
                        return export("chunk",{"data":f" ::: Language: {calls[-1]['language']} :::\n\n", "type":"function_call"})

                print("44444444444444444444444 OPEN CLOSE BOX")
                
                return export("chunk",{"data":"", "type":"function_call", "payload":delta})#,{"role":payload["role"]}) 
                #return export("chunk",{"data":delta["function_call"]["arguments"], "type":"function_call", "payload":delta})#,{"role":payload["role"]}) 
            
            
            
            
            else:
                return export("chunk",{"data":delta["function_call"], "type":"unknown_function_call"})#,{"role":payload["role"]})
                print("> > ????????????????????",delta)
        if not found:
            return export("unknown",{"payload":data, "type":"unknown"})#,{"role":payload["role"]})
            print("> > !!!!!!!!! ????????????????????",data)
            
        

