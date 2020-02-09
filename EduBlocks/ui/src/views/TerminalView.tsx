import React = require('preact');
import { Component } from 'preact';

import { TerminalInterface, TerminalEvents } from '../types';

interface TerminalViewProps {
  visible: boolean;

  onClose(): void;
}

const stub = () => void 0;

export default class TerminalView extends Component<TerminalViewProps, {}> implements TerminalInterface {
  private termDiv?: Element;
  private term: Terminal;

  public cols: number;
  public rows: number;

  private eventHandlers: TerminalEvents = {
    data: stub,
    resize: stub,
  };

  private fit() {
    this.term.fit();

    if (this.cols !== this.term.cols || this.rows !== this.term.rows) {
      this.cols = this.term.cols;
      this.rows = this.term.rows;

      this.eventHandlers.resize(this.cols, this.rows);
    }
  }

  protected componentDidMount() {
    if (!this.termDiv) throw new Error('No term');

    this.term = new Terminal();

    this.term.open(this.termDiv, true);

    this.term.on('data', (data) => {
      this.eventHandlers.data(data);

      if (data.length === 1 && data.charCodeAt(0) === 27) {
        this.props.onClose();
      }
    });

    this.term.write('\x1b[31mWelcome to EduBlocks!\x1b[m\r\n');
    this.term.write('Press [ESC] to exit the terminal\r\n');

    this.fit();

    window.addEventListener('resize', () => this.fit());
  }

  protected componentDidUpdate() {
    this.fit();
  }

  public focus() {
    if (!this.term) return;

    this.term.focus();
  }

  public reset() {
    console.info('RESET TERM');

    this.term.reset();
  }

  public write(s: string) {
    this.term.write(s);
  }

  public on<K extends keyof TerminalEvents>(eventType: K, handler: TerminalEvents[K]) {
    this.eventHandlers[eventType] = handler;
  }

  public onCloseClick() {
    this.props.onClose();
  }

  public onStopClick() {
    // Send Ctrl+C
    this.eventHandlers.data('\x03');
  }

  public render() {
    return (
      <div style={{ display: this.props.visible ? 'block' : 'none' }} id="terminal-dialog">
        <div class="terminal-help">
          <span class="help-item" onClick={() => this.onCloseClick()}>
            <span class="key">ESC</span> = Close terminal
          </span>
          <span class="help-item" onClick={() => this.onStopClick()}>
            <span class="key">Ctrl</span> + <span class="key">C</span> = Stop program
          </span>
        </div>
        <div id="term" ref={(div) => this.termDiv = div}></div>
      </div>
    );
  }
}
