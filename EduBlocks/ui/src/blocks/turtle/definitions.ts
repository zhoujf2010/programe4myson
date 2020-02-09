export default function define(Blocks: Blockly.BlockDefinitions) {
  Blocks['import_turtle'] = {
    init: function() {
      this.appendDummyInput()
          .appendField("from turtle import *");
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setColour(240);
   this.setTooltip("Import Turtle library");
   this.setHelpUrl("");
    }
  };

  Blocks['turtle'] = {
    init: function() {
      this.appendDummyInput()
          .appendField(new Blockly.FieldVariable("turtle"), "turtle")
          .appendField(" = Turtle()");
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setColour(240);
   this.setTooltip("Initialize the turtle");
   this.setHelpUrl("");
    }
  };

  Blocks['screeninit'] = {
    init: function() {
      this.appendDummyInput()
          .appendField(new Blockly.FieldVariable("screen"), "wn")
          .appendField(" = Screen()");
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setColour(240);
   this.setTooltip("Initialize the Turtle screen");
   this.setHelpUrl("");
    }
  };

  Blocks['background'] = {
    init: function() {
      this.appendDummyInput()
          .appendField(new Blockly.FieldVariable("wn"), "wn")
          .appendField(".bgcolour(")
          .appendField(new Blockly.FieldTextInput("\"red\""), "color")
          .appendField(")");
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setColour(240);
   this.setTooltip("Change the background");
   this.setHelpUrl("");
    }
  };

  Blocks['directions'] = {
    init: function() {
      this.appendDummyInput()
          .appendField(new Blockly.FieldVariable("turtle"), "turtle")
          .appendField(".")
          .appendField(new Blockly.FieldDropdown([["forward","forward"], ["left","left"], ["right","right"], ["backward","backward"]]), "options")
          .appendField("(")
          .appendField(new Blockly.FieldTextInput(""), "dist")
          .appendField(")");
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setColour(240);
   this.setTooltip("Make the turtle move");
   this.setHelpUrl("");
    }
  };

  Blocks['penud'] = {
    init: function() {
      this.appendDummyInput()
          .appendField(new Blockly.FieldVariable("turtle"), "turtle")
          .appendField(".pen")
          .appendField(new Blockly.FieldDropdown([["up","up"], ["down","down"]]), "options")
          .appendField("()");
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setColour(240);
   this.setTooltip("Pen up and down");
   this.setHelpUrl("");
    }
  };

  Blocks['pen'] = {
    init: function() {
      this.appendDummyInput()
          .appendField(new Blockly.FieldVariable("turtle"), "turtle")
          .appendField(".pen()");
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setColour(240);
   this.setTooltip("Initialize the pen");
   this.setHelpUrl("");
    }
  };

  Blocks['colourpen'] = {
    init: function() {
      this.appendDummyInput()
          .appendField(new Blockly.FieldVariable("turtle"), "turtle")
          .appendField(".pencolor(")
          .appendField(new Blockly.FieldTextInput(""), "dist")
          .appendField(")");
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setColour(240);
   this.setTooltip("Change the colour");
   this.setHelpUrl("");
    }
  };

  Blocks['colour'] = {
    init: function() {
      this.appendDummyInput()
          .appendField(new Blockly.FieldVariable("turtle"), "turtle")
          .appendField(".color(")
          .appendField(new Blockly.FieldTextInput(""), "dist")
          .appendField(")");
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setColour(240);
   this.setTooltip("Change the colour");
   this.setHelpUrl("");
    }
  };

  Blocks['colourmode'] = {
    init: function() {
      this.appendDummyInput()
          .appendField(new Blockly.FieldVariable("screen"), "wn")
          .appendField(".colormode(")
          .appendField(new Blockly.FieldTextInput(""), "dist")
          .appendField(")");
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setColour(240);
   this.setTooltip("Change the colourmode");
   this.setHelpUrl("");
    }
  };

  Blocks['penwidth'] = {
    init: function() {
      this.appendDummyInput()
          .appendField(new Blockly.FieldVariable("turtle"), "turtle")
          .appendField(".width(")
          .appendField(new Blockly.FieldTextInput(""), "dist")
          .appendField(")");
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setColour(240);
   this.setTooltip("Change the width");
   this.setHelpUrl("");
    }
  };

  Blocks['circle'] = {
    init: function() {
      this.appendDummyInput()
          .appendField(new Blockly.FieldVariable("turtle"), "turtle")
          .appendField(".circle(")
          .appendField(new Blockly.FieldTextInput(""), "dist")
          .appendField(")");
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setColour(240);
   this.setTooltip("Draw a circle");
   this.setHelpUrl("");
    }
  };

  Blocks['goto'] = {
    init: function() {
      this.appendDummyInput()
          .appendField(new Blockly.FieldVariable("turtle"), "turtle")
          .appendField(".goto(")
          .appendField(new Blockly.FieldTextInput(""), "dist")
          .appendField(")");
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setColour(240);
   this.setTooltip("go to x&y");
   this.setHelpUrl("");
    }
  };
}
