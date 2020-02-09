import React = require('preact');
import { Component } from 'preact';

import Nav from './Nav';
import BlocklyView from './BlocklyView';
import BothView from './BothView';
import PythonView from './PythonView';
import TerminalView from './TerminalView';
import SelectModal from './SelectModal';

import { App } from '../types';

const ViewModeBlockly = 'blockly';
const ViewModePython = 'python';
const ViewModeBoth = 'both';

type ViewMode = typeof ViewModeBlockly | typeof ViewModePython | typeof ViewModeBoth;

interface PageProps {
  app: App;
}

interface DocumentState {
  xml: string | null;
  python: string | null;
  pythonClean: boolean;
}

interface PageState {
  viewMode: ViewMode;
  terminalOpen: boolean;
  samplesOpen: boolean;
  themesOpen: boolean;

  doc: Readonly<DocumentState>;
}

export default class Page extends Component<PageProps, PageState> {
  private blocklyView: BlocklyView;
  private pythonView: PythonView;
  private bothView: BothView;
  public terminalView: TerminalView;

  constructor() {
    super();

    this.state = {
      viewMode: ViewModeBoth,
      terminalOpen: false,
      samplesOpen: false,
      themesOpen: false,

      doc: {
        xml: null,
        python: null,
        pythonClean: true,
      },
    };
  }

  private readBlocklyContents(xml: string) {
    if (this.state.doc.xml === xml) { return; }

    const doc: DocumentState = {
      xml,
      python: null,
      pythonClean: true,
    };

    this.setState({ doc });

    this.switchView(ViewModeBoth);
  }

  private updateFromBlockly(xml: string, python: string) {
    if (
      this.state.doc.xml === xml &&
      this.state.doc.python === python
    ) {
      return;
    }

    if (this.state.doc.python !== python && !this.state.doc.pythonClean) {
      alert('Python changes have been overwritten!');
    }

    const doc: DocumentState = {
      xml,
      python,
      pythonClean: true,
    };

    this.setState({ doc });
  }

  private updateFromPython(python: string) {
    if (this.state.doc.python === python) { return; }

    const doc: DocumentState = {
      xml: this.state.doc.xml,
      python,
      pythonClean: false,
    };

    this.setState({ doc });
  }

  private updateFromBloth(xml: string, python: string) {
    if (
      this.state.doc.xml === xml &&
      this.state.doc.python === python
    ) {
      return;
    }

    if (this.state.doc.python !== python && !this.state.doc.pythonClean) {
      alert('Python changes have been overwritten!');
    }
    const doc: DocumentState = {
      xml,
      python,
      pythonClean: true,
    };
    this.state.doc = doc;
  }


  private new() {
    const doc: DocumentState = {
      xml: null,
      python: null,
      pythonClean: true,
    };

    this.setState({ doc });

    this.switchView('blockly');
  }

  protected componentDidMount() {

  }

  private toggleView(): 0 {
    switch (this.state.viewMode) {
      case ViewModeBlockly:
        return this.switchView(ViewModePython);

      case ViewModePython:
        return this.switchView(ViewModeBoth);

      case ViewModeBoth:
        return this.switchView(ViewModeBlockly);
    }
  }

  private switchView(viewMode: ViewMode): 0 {
    switch (viewMode) {
      case ViewModeBlockly:
        this.setState({ viewMode: 'blockly' });

        return 0;

      case ViewModePython:
        this.setState({ viewMode: 'python' });

        return 0;

      case ViewModeBoth:
        this.setState({ viewMode: 'both' });

        return 0;
    }
  }

  private sendCode() {
    if (!this.terminalView) { throw new Error('No terminal'); }

    if (!this.state.doc.python) {
      alert('未编写代码，无法运行');

      return;
    }
    this.bothView.changeXML();
    this.setState({ terminalOpen: true });
    this.terminalView.focus();
    this.terminalView.reset();

    this.props.app.runCode(this.state.doc.python);

    setTimeout(() => this.terminalView.focus(), 250);
  }

  private onBlocklyChange(xml: string, python: string) {
    this.updateFromBlockly(xml, python);
  }

  private onPythonChange(python: string) {
    this.updateFromPython(python);
  }

  private onBothChange(xml: string, python: string) {
    this.updateFromBloth(xml, python);
  }

  private async openFile() {
    const xml = await this.props.app.openFile(this.props.app);
    var filename = this.props.app.currentFile;
    document.title = filename;
    this.readBlocklyContents(xml);
  }

  private async saveFile() {
    const xml = this.state.doc.xml;

    var filename = document.title;
    if (filename =='EduBlocks')
      filename ="";
    if (xml) {
      await this.props.app.saveFile(xml, 'xml',filename);
    }
  }

  private async downloadPython() {
    const python = this.state.doc.python;

    if (python) {
      await this.props.app.saveFile(python, 'py','');
    }
  }

  private openSamples() {
    this.setState({ samplesOpen: true });
  }

  private closeSamples() {
    this.setState({ samplesOpen: false });
  }

  private selectSample(file: string) {
    this.closeSamples();

    const xml = this.props.app.getSample(file);

    this.readBlocklyContents(xml);
  }

  private openThemes() {
    this.setState({ themesOpen: true });
  }

  private closeThemes() {
    this.setState({ themesOpen: false });
  }

  private selectTheme(theme: string) {
    this.closeThemes();

    document.body.className = `theme-${theme}`;
  }

  private onTerminalClose() {
    this.setState({ terminalOpen: false });
  }

  public render() {
    return (
      <div id='page'>
        <Nav
          sync={this.state.doc.pythonClean}

          sendCode={() => this.sendCode()}
          downloadPython={() => this.downloadPython()}
          openCode={() => this.openFile()}
          saveCode={() => this.saveFile()}
          newCode={() => this.new()}
          openSamples={() => this.openSamples()}
          openThemes={() => this.openThemes()} />

        <section id='workspace'>
          <button
            id='toggleViewButton'
            onClick={() => this.toggleView()}>

            {this.state.viewMode}

          </button>

          <BlocklyView
            ref={(c) => this.blocklyView = c}
            visible={this.state.viewMode === 'blockly'}
            xml={this.state.doc.xml}
            onChange={(xml, python) => this.onBlocklyChange(xml, python)} />

          <PythonView
            ref={(c) => this.pythonView = c}
            visible={this.state.viewMode === 'python'}
            python={this.state.doc.python}
            onChange={(python) => this.onPythonChange(python)} />

          <BothView
            ref={(c) => this.bothView = c}
            visible={this.state.viewMode === 'both'}
            xml={this.state.doc.xml}
            python={this.state.doc.python}
            fromwho=''
            onChange={(xml, python) => this.onBothChange(xml, python)}
          />
        </section>

        <TerminalView
          ref={(c) => this.terminalView = c}
          visible={this.state.terminalOpen}
          onClose={() => this.onTerminalClose()} />

        <SelectModal
          title='Samples'
          options={this.props.app.getSamples()}
          visible={this.state.samplesOpen}
          onSelect={(file) => this.selectSample(file)}
          onCancel={() => this.closeSamples()} />

        <SelectModal
          title='Themes'
          options={this.props.app.getThemes()}
          visible={this.state.themesOpen}
          onSelect={(theme) => this.selectTheme(theme)}
          onCancel={() => this.closeThemes()} />
      </div>
    );
  }
}
