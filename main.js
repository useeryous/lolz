const { app, BroswerWindow } = require('electron')

const createWindow = () => {
    const win = new BroswerWindow({
        width: 800,
        height: 600
    })

    win.loadFile('./src/htmlSrc/index.html')
}

app.whenReady().then(() => {
    createWindow()

    app.on('activate', () => {
        if (BroswerWindow.getAllWindows().length === 0) {
            createWindow()
        }
    })
})

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
        app.quit()
    }
})