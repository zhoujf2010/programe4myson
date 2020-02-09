export default function define(Blocks: Blockly.BlockDefinitions) {
  Blocks['connect'] = {
    init: function () {
      this.appendDummyInput()
        .appendField("连接WeDo");
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setColour(290);
      this.setTooltip("Import Turtle library");
      this.setHelpUrl("");
    }
  };

  Blocks['motoron'] = {
    init: function () {
      this.appendDummyInput()
        .appendField("启动马达,功率为")
      this.appendValueInput('val');
      this.appendDummyInput()
        .appendField(" ")
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setColour(290);
      this.setHelpUrl("");
    }
  };

  Blocks['motoroff'] = {
    init: function () {
      this.appendDummyInput()
        .appendField("关闭马达");
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setColour(290);
      this.setTooltip("Import Turtle library");
      this.setHelpUrl("");
    }
  };

  Blocks['disconnect'] = {
    init: function () {
      this.appendDummyInput()
        .appendField("断开WeDo");
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setColour(290);
      this.setTooltip("Import Turtle library");
      this.setHelpUrl("");
    }
  };

  Blocks['distnace'] = {
    init: function () {
      this.appendDummyInput()
        .appendField("距离");
      this.setColour(290);
      this.setOutput(true, 'var');
      this.setTooltip("Import Turtle library");
      this.setHelpUrl("");
    }
  };

  Blocks['tiltX'] = {
    init: function () {
      this.appendDummyInput()
        .appendField("倾斜度X");
      this.setColour(290);
      this.setOutput(true, 'var');
      this.setTooltip("Import Turtle library");
      this.setHelpUrl("");
    }
  };

  Blocks['tiltY'] = {
    init: function () {
      this.appendDummyInput()
        .appendField("倾斜度Y");
      this.setColour(290);
      this.setOutput(true, 'var');
      this.setTooltip("Import Turtle library");
      this.setHelpUrl("");
    }
  };


  Blocks['ev3connect'] = {
    init: function () {
      this.appendDummyInput()
        .appendField("连接EV3");
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setColour(240);
      this.setTooltip("Import Turtle library");
      this.setHelpUrl("");
    }
  };

  Blocks['ev3disconnect'] = {
    init: function () {
      this.appendDummyInput()
        .appendField("断开EV3");
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setColour(240);
      this.setTooltip("Import Turtle library");
      this.setHelpUrl("");
    }
  };

  Blocks['ev3motoron'] = {
    init: function () {
      this.appendDummyInput()
        .appendField("启动马达[")
        .appendField(new Blockly.FieldDropdown([['A', 'A'], ['B', 'B'], ['C', 'C'], ['D', 'D']]), 'port')
        .appendField("],功率为")
      this.appendValueInput('val');
      this.appendDummyInput()
        .appendField(" ")
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setColour(240);
      this.setHelpUrl("");
    }
  };

  Blocks['ev3motordegree'] = {
    init: function () {
      this.appendDummyInput()
        .appendField("马达[")
        .appendField(new Blockly.FieldDropdown([['A', 'A'], ['B', 'B'], ['C', 'C'], ['D', 'D']]), 'port')
        .appendField("],转至")
      this.appendValueInput('degree');
      this.appendDummyInput()
      .appendField("度,功率为")
      this.appendValueInput('val');
      this.appendDummyInput()
        .appendField(" ")
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setColour(240);
      this.setHelpUrl("");
    }
  };

  Blocks['ev3motorpos'] = {
    init: function () {
      this.appendDummyInput()
        .appendField("马达[")
        .appendField(new Blockly.FieldDropdown([['A', 'A'], ['B', 'B'], ['C', 'C'], ['D', 'D']]), 'port')
        .appendField("]的位置");
      this.setColour(240);
      this.setOutput(true, 'var');
      this.setTooltip("Import Turtle library");
      this.setHelpUrl("");
    }
  };

  Blocks['ev3motoroff'] = {
    init: function () {
      this.appendDummyInput()
        .appendField("关闭[")
        .appendField(new Blockly.FieldDropdown([['A', 'A'], ['B', 'B'], ['C', 'C'], ['D', 'D']]), 'port')
        .appendField("]马达,刹车")
        .appendField(new Blockly.FieldCheckbox('TRUE'), 'brake');
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setColour(240);
      this.setTooltip("Import Turtle library");
      this.setHelpUrl("");
    }
  };

  Blocks['ev3ultradistance'] = {
    init: function () {
      this.appendDummyInput()
        .appendField("[")
        .appendField(new Blockly.FieldDropdown([['1', '1'], ['2', '2'], ['3', '3'], ['4', '4']]), 'port')
        .appendField("]超声波距离");
      this.setColour(240);
      this.setOutput(true, 'var');
      this.setTooltip("Import Turtle library");
      this.setHelpUrl("");
    }
  };

  Blocks['ev3touchispressed'] = {
    init: function () {
      this.appendDummyInput()
        .appendField("[")
        .appendField(new Blockly.FieldDropdown([['1', '1'], ['2', '2'], ['3', '3'], ['4', '4']]), 'port')
        .appendField("]按钮是否按下");
      this.setColour(240);
      this.setOutput(true, 'var');
      this.setTooltip("Import Turtle library");
      this.setHelpUrl("");
    }
  };

  Blocks['ev3touchwaitpressed'] = {
    init: function () {
      this.appendDummyInput()
        .appendField("[")
        .appendField(new Blockly.FieldDropdown([['1', '1'], ['2', '2'], ['3', '3'], ['4', '4']]), 'port')
        .appendField("]按钮待等按下");
      this.setColour(240);
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setColour(240);
      this.setHelpUrl("");
    }
  };

  Blocks['ev3touchwaitreleased'] = {
    init: function () {
      this.appendDummyInput()
        .appendField("[")
        .appendField(new Blockly.FieldDropdown([['1', '1'], ['2', '2'], ['3', '3'], ['4', '4']]), 'port')
        .appendField("]按钮待等弹出");
      this.setColour(240);
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setColour(240);
      this.setHelpUrl("");
    }
  };

  Blocks['ev3colorambient'] = {
    init: function () {
      this.appendDummyInput()
        .appendField("[")
        .appendField(new Blockly.FieldDropdown([['1', '1'], ['2', '2'], ['3', '3'], ['4', '4']]), 'port')
        .appendField("]环境光强度");
      this.setColour(240);
      this.setOutput(true, 'var');
      this.setTooltip("Import Turtle library");
      this.setHelpUrl("");
    }
  };

  Blocks['ev3colorreflected'] = {
    init: function () {
      this.appendDummyInput()
        .appendField("[")
        .appendField(new Blockly.FieldDropdown([['1', '1'], ['2', '2'], ['3', '3'], ['4', '4']]), 'port')
        .appendField("]反射光强度");
      this.setColour(240);
      this.setOutput(true, 'var');
      this.setTooltip("Import Turtle library");
      this.setHelpUrl("");
    }
  };

  Blocks['ev3colordetect'] = {
    init: function () {
      this.appendDummyInput()
        .appendField("[")
        .appendField(new Blockly.FieldDropdown([['1', '1'], ['2', '2'], ['3', '3'], ['4', '4']]), 'port')
        .appendField("]颜色检测");
      this.setColour(240);
      this.setOutput(true, 'var');
      this.setTooltip("Import Turtle library");
      this.setHelpUrl("");
    }
  };

  Blocks['ev3colordetect2'] = {
    init: function () {
      this.appendDummyInput()
        .appendField("[")
        .appendField(new Blockly.FieldDropdown([['1', '1'], ['2', '2'], ['3', '3'], ['4', '4']]), 'port')
        .appendField("]颜色检测2");
      this.setColour(240);
      this.setOutput(true, 'var');
      this.setTooltip("Import Turtle library");
      this.setHelpUrl("");
    }
  };

  Blocks['ev3gyroangle'] = {
    init: function () {
      this.appendDummyInput()
        .appendField("[")
        .appendField(new Blockly.FieldDropdown([['1', '1'], ['2', '2'], ['3', '3'], ['4', '4']]), 'port')
        .appendField("]陀螺仪角度");
      this.setColour(240);
      this.setOutput(true, 'var');
      this.setTooltip("Import Turtle library");
      this.setHelpUrl("");
    }
  };

  Blocks['ev3gyrorate'] = {
    init: function () {
      this.appendDummyInput()
        .appendField("[")
        .appendField(new Blockly.FieldDropdown([['1', '1'], ['2', '2'], ['3', '3'], ['4', '4']]), 'port')
        .appendField("]陀螺仪转角速度");
      this.setColour(240);
      this.setOutput(true, 'var');
      this.setTooltip("Import Turtle library");
      this.setHelpUrl("");
    }
  };

  Blocks['ev3playsoundfile'] = {
    init: function () {
      this.appendDummyInput()
        .appendField("播放声音")
        .appendField(new Blockly.FieldTextInput(''), 'filename')
        .appendField("响度为")
        .appendField(new Blockly.FieldTextInput('100'), 'sound');
      this.setColour(240);
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setTooltip("Import Turtle library");
      this.setHelpUrl("");
    }
  };

  Blocks['ev3displayimage'] = {
    init: function () {
      this.appendDummyInput()
      .appendField("显示屏幕")
      .appendField(new Blockly.FieldTextInput(''), 'filename');
      this.setColour(240);
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setTooltip("Import Turtle library");
      this.setHelpUrl("");
    }
  };
}
