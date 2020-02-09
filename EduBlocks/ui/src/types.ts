interface App {
  runCode(code: string): void;

  openFile(app:App): Promise<string>;
  saveFile(code: string, ext: string,filename:string): Promise<void>;

  assignTerminal(term: TerminalInterface): void;

  getThemes(): string[];

  getSamples(): string[];
  getSample(file: string): string;
  
  currentFile:string;
}

interface TerminalEvents {
  data: (data: string) => void;
  resize: (cols: number, rows: number) => void;
}

interface TerminalInterface {
  on<K extends keyof TerminalEvents>(eventType: K, handler: TerminalEvents[K]): void;

  focus(): void;
  write(s: string): void;
  reset(): void;

  cols: number;
  rows: number;
}

export {
  App,
  TerminalEvents,
  TerminalInterface,
};
