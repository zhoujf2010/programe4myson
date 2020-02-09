export default function define(Blocks: Blockly.BlockDefinitions) {
  Blocks['importmb'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("import microbit");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(290);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};
Blocks['displayscrolltext'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("microbit.display.scroll(\"")
        .appendField(new Blockly.FieldTextInput(""), "message")
        .appendField("\")");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(290);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};

Blocks['displayscrollvar'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("microbit.display.scroll(")
        .appendField(new Blockly.FieldTextInput(""), "varmess")
        .appendField(")");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(290);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};

Blocks['microsleep'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("microbit.sleep(")
        .appendField(new Blockly.FieldTextInput(""), "time")
        .appendField(")");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(290);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};

Blocks['displayshow'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("microbit.display.show(")
        .appendField(new Blockly.FieldTextInput(""), "show")
        .appendField(")");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(290);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};

Blocks['displayclear'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("microbit.display.clear()");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(290);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};

  
}
