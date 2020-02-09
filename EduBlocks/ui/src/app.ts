import { newServer } from './server';
import { App, TerminalInterface } from './types';
import { getIo } from './io';
import { newSamples } from './samples';

async function newApp(): Promise<App> {
  const client = await newServer();
  const io = getIo();
  const samples = newSamples();
  var currentFile = "";

  function runCode(code: string) {
    return client.runCode(code);
  }

  function openFile(app:App) {
    return io.openFile(app);
  }

  function saveFile(data: string, ext: string,filename:string) {
    return io.saveFile(data, ext,filename);
  }

  function assignTerminal(terminal: TerminalInterface) {
    client.on('data', (data) => terminal.write(data));

    client.on('reconnect', () => {
      terminal.reset();

      client.resizeTerminal(terminal.cols, terminal.rows);
    });

    terminal.on('data', client.sendData);
    terminal.on('resize', client.resizeTerminal);

    if (terminal.cols && terminal.rows) {
      client.resizeTerminal(terminal.cols, terminal.rows);
    }
  }

  function getThemes() {
    return [
      'Default',
      'Tangerine',
      'DarkRed',
      'Celestial',
      'Pacific',
      'Dark',
    ];
  }

  return {
    runCode,
    openFile,
    saveFile,
    assignTerminal,
    getThemes,
    ...samples,
    currentFile
  };
}

export {
  newApp,
};
