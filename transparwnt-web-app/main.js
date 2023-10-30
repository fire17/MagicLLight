const { app, BrowserWindow, globalShortcut } = require('electron');
let win
app.on('blur', () => {
	
});
function onTop(){
setTimeout(() => {
		win.setAlwaysOnTop(true);
		onTop();
	  }, 100); 
}
	  
app.on('ready', () => {
  win = new BrowserWindow({
    width: 1920, // Set your desired width
    height: 1080, // Set your desired height
    frame: false, // No window frame
    transparent: true, // Make the window transparent
    webPreferences: {
      nodeIntegration: true,
    },
  });

  // Make the window fullscreen
  win.setFullScreen(true);

  // Hide the app icon in the OS taskbar (for all platforms)
  win.setSkipTaskbar(true);

  // Always keep the window on top of other windows
  win.setAlwaysOnTop(true);

  win.loadFile('index_working.html');
  //onTop();

});
