import React = require('preact');
import { Component } from 'preact';

interface SelectModalProps {
  title: string;
  visible: boolean;
  options: string[];

  onCancel(): void;
  onSelect(option: string): void;
}

interface SelectModalState {

}

export default class SelectModal extends Component<SelectModalProps, SelectModalState> {
  public render() {
    const getOptions = () => this.props.options.map((option) => (
      <tr>
        <td>{option}</td>
        <td><button onClick={() => this.props.onSelect(option)}>Select</button></td>
      </tr>
    ));

    return (
      <div class='modal'>
        <input id='modal_1' type='checkbox' disabled={true} checked={this.props.visible} />
        <label for='modal_1' class='overlay'></label>
        <article>
          <header>
            <h3>{this.props.title}</h3>
            <a class='close' onClick={this.props.onCancel}>&times;</a>
          </header>
          <section class='content'>
            <table class='primary'>
              <tbody>
                {getOptions()}
              </tbody>
            </table>
          </section>
          <footer>
            <button onClick={this.props.onCancel}>Close</button>
          </footer>
        </article>
      </div>
    );
  }
}
