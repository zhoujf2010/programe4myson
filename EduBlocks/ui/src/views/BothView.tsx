import React = require('preact');
import { Component } from 'preact';
import { getToolBoxXml } from '../blocks';
import _ = require('lodash');

const Blockly2 = (self as any).Blockly;
const ace2 = (self as any).ace;

interface BothViewProps {
  visible: boolean;
  xml: string | null;
  python: string | null;
  fromwho : String |null;

  //onChangexml(xml: string, python: string): void;
  onChange(xml: string, python: string): void;
}

export default class BothView extends Component<BothViewProps, {}> {
  private Blockly2Div?: Element;
  private xml: string | null;
  
  private editorDiv?: Element;
  private editor: any;

  protected componentWillReceiveProps(nextProps: BothViewProps) {
    if (nextProps.visible) {
      if (this.xml !== nextProps.xml) {
        this.setXml(nextProps.xml);
      }
    }
	
    if (nextProps.visible) {
      // Need to check visible change as well to force refresh
      if (this.getCode() !== nextProps.python || this.props.visible !== nextProps.visible) {
        this.setCode(nextProps.python);
      }
    }
  }

  public changeXML(){
    const xml = this.getXml();
    const python = this.getPython();

    this.xml = xml;
    this.props.fromwho='xml';
    this.props.onChange(xml, python);
    this.setCode(python);
  }

  protected async componentDidMount() {
    if (this.Blockly2Div) {
      const toolbox = getToolBoxXml();

      const workspace = Blockly2.inject(this.Blockly2Div, {
        media: 'Blockly/media/',
        toolbox,
      });

      workspace.addChangeListener((e : Object) => {
		if (this.props.fromwho == 'python'){
			this.props.fromwho='';
			return;
		}
		if (JSON.stringify(e).indexOf("oldCoordinate")<0)
			return;//not put element down
        const xml = this.getXml();
        const python = this.getPython();

        this.xml = xml;
		this.props.fromwho='xml';
        this.props.onChange(xml, python);
		this.setCode(python);
      });

      Blockly2.svgResize(workspace);
    }
	
	
    if (!this.editorDiv) { throw new Error('No editor div'); }

    this.editor = ace2.edit(this.editorDiv);

    this.editor.setTheme('ace/theme/monokai');
    this.editor.getSession().setMode('ace/mode/python');

    this.editor.on('blur', _.debounce(() => {
		if (this.props.fromwho == 'xml'){
			this.props.fromwho='';
			return;
		}
		  
		const code = this.getCode();
		//TODO python to xml
        const xml = this.getXml();
        //const xml = "<xml></xml>";
		
		//console.log("-->" + code);
		this.props.fromwho='python';
		this.props.onChange(xml,code);
		this.setXml(xml);
    }, 100));
  }
  
  private getCode(): string {
    return this.editor.getValue();
  }

  private setCode(code: string | null) {
    this.editor.setValue(code || '');
    this.editor.clearSelection();
  }

  private getXml(): string {
    const xml = Blockly2.Xml.workspaceToDom(Blockly2.mainWorkspace);

    return Blockly2.Xml.domToPrettyText(xml);
  }

  private getPython(): string {
    return Blockly2.Python.workspaceToCode();
  }

  private setXml(xml: string | null) {
    Blockly2.mainWorkspace.clear();

    if (typeof xml === 'string') {
      const textToDom = Blockly2.Xml.textToDom(xml);
      Blockly2.Xml.domToWorkspace(textToDom, Blockly2.mainWorkspace);
    }
  }

  public render() {
    return (
	<div id='both' style={{ display: this.props.visible ? 'block' : 'none' }}>
      <div
        id='both_left'
        ref={(div) => this.Blockly2Div = div}>
      </div>
      <div
        id='both_right'
		ref={(div) => this.editorDiv = div}
        >
      </div>
    </div>
    );
  }
}
