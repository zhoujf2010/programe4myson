export default function define(Blocks: Blockly.BlockDefinitions) {
  Blocks['import_sonic'] = {
    init: function () {
      this.appendDummyInput()
        .appendField('from psonic import *');
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setColour(180);
      this.setTooltip('');
      this.setHelpUrl('');
    },
  };

  Blocks['sampleson'] = {
    init: function () {
      this.appendDummyInput()
        .appendField('sample(')
        .appendField(new Blockly.FieldTextInput('name'), 'name')
        .appendField(')');
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setColour(180);
      this.setTooltip('');
      this.setHelpUrl('');
    },
  };

  Blocks['play'] = {
    init: function () {
      this.appendDummyInput()
        .appendField('play(')
        .appendField(new Blockly.FieldTextInput('0'), 'value')
        .appendField(')');
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setColour(180);
      this.setTooltip('Play a single note');
      this.setHelpUrl('');
    },
  };

  Blocks['sleep1'] = {
    init: function () {
      this.appendDummyInput()
        .appendField('sleep(')
        .appendField(new Blockly.FieldTextInput('0'), 'value')
        .appendField(')');
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setColour(180);
      this.setTooltip('Play a single note');
      this.setHelpUrl('');
    },
  };

  Blocks['liveloop'] = {
    init: function () {
      this.appendDummyInput()
        .appendField('live_loop_')
        .appendField(new Blockly.FieldDropdown([['1', '1'], ['2', '2'], ['3', '3'], ['4', '4']]), 'num');
      this.appendStatementInput('DO')
        .setCheck(null);
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setColour(180);
      this.setTooltip('Create a live loop with Sonic Pi');
      this.setHelpUrl('');
    },
  };
}
