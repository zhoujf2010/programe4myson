import React = require('preact');
import { Component } from 'preact';

interface NavProps {
  openSamples(): void;
  openThemes(): void;
  downloadPython(): void;

  newCode(): void;
  openCode(): void;
  saveCode(): void;
  sendCode(): void;

  sync: boolean;
}

export default class Nav extends Component<NavProps, {}> {
  public render() {
    return (
      <nav>
        <a class='brand'>
          <img class='logo' src='/images/logo.png' />
          <span>EduBlocks</span>
          {/*<span class='filename'>({this.props.sync ? 'In sync' : 'Out of sync'})</span>*/}
        </a>

        <input id='bmenub' type='checkbox' class='show' />
        <label for='bmenub' class='burger pseudo button'>menu</label>

        <div class='menu'>
          <a class='button' title='Themes' href='javascript:void(0)' onClick={() => this.props.openThemes()}>
            主题
          </a>

          <a class='button' title='Samples' href='javascript:void(0)' onClick={() => this.props.openSamples()}>
            样例
          </a>

          <a class='button icon-download' title='Download Python Source Code' href='javascript:void(0)' onClick={() => this.props.downloadPython()}>
            下载python代码
          </a>

          <a class='button icon-plus' title='New' href='javascript:void(0)' onClick={() => this.props.newCode()}>
            新建
          </a>

          <a class='button icon-folder-open' title='Open a file' href='javascript:void(0)' onClick={() => this.props.openCode()}>
            打开
          </a>

          <a class='button icon-floppy' title='Save a file' href='javascript:void(0)' onClick={() => this.props.saveCode()}>
            保存
          </a>

          <a class='button icon-play' title='Run your code' href='javascript:void(0)' onClick={() => this.props.sendCode()}>
            运行
          </a>
        </div>
      </nav>
    );
  }
}
