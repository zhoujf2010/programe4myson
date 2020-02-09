export default function define(Blocks: Blockly.BlockDefinitions) {


  Blocks['const_value'] = {
    init: function () {
      this.appendDummyInput()
        .appendField(new Blockly.FieldTextInput(''), 'var');
	  
      this.setPreviousStatement(false, null);
      this.setNextStatement(false, null);
      this.setOutput(true, 'var');
      this.setTooltip('Use this to print to the output box.');
      this.setHelpUrl('http://www.example.com/');
      this.setColour(70);
    }, 
  };

  Blocks['const_txt'] = {
    init: function () {
      this.appendDummyInput()
        .appendField('"')
        .appendField(new Blockly.FieldTextInput(''), 'var')
        .appendField('"');
	  
      this.setPreviousStatement(false, null);
      this.setNextStatement(false, null);
      this.setOutput(true, 'var');
      this.setTooltip('Use this to print to the output box.');
      this.setHelpUrl('http://www.example.com/');
      this.setColour(70);
    }, 
  };


  Blocks['basic_print'] = {
    init: function () {
      this.appendDummyInput()
        .appendField('打印');
      this.appendValueInput('VALUE');
	  
      this.setInputsInline(true);
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setTooltip('Use this to print to the output box.');
      this.setHelpUrl('http://www.example.com/');
      this.setColour(70);
    },
  };


  Blocks['basic_input'] = {
    init: function () {
      this.appendDummyInput()
      .appendField('输入')
        .appendField(new Blockly.FieldTextInput(''), 'var');
	  
      this.setPreviousStatement(false, null);
      this.setNextStatement(false, null);
      this.setOutput(true, 'var');
      this.setTooltip('Use this to print to the output box.');
      this.setHelpUrl('http://www.example.com/');
      this.setColour(70);
    },
  };

  Blocks['math_arithmetic'] = {
    init: function () {
      this.appendValueInput('A');
      this.appendDummyInput()
        .appendField(new Blockly.FieldDropdown([['加', '+'], ['减', '-'], ['乘', '*'], ['除', '/'], ['幂', '^'], ['模', '%']]), 'crocsigns');
      this.appendValueInput('B');
	  
      this.setPreviousStatement(false, null);
      this.setNextStatement(false, null);
      this.setOutput(true, 'Number');
      this.setTooltip('Use this to print to the output box.');
      this.setHelpUrl('http://www.example.com/');
      this.setColour(70);
    },
  };

  Blocks['math_single'] = {
    init: function () {
      this.appendDummyInput()
        .appendField(new Blockly.FieldDropdown([['绝对值', 'abs'], ['开根', 'sqrt']]), 'crocsigns');
      this.appendValueInput('A');
	  
      this.setPreviousStatement(false, null);
      this.setNextStatement(false, null);
      this.setOutput(true, 'Number');
      this.setTooltip('Use this to print to the output box.');
      this.setHelpUrl('http://www.example.com/');
      this.setColour(70);
    },
  };

  Blocks['sleep'] = {
    init: function () {
      this.appendDummyInput()
        .appendField('停顿')
      this.appendValueInput('sleepTime');
      this.appendDummyInput()
        .appendField('秒');
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setColour(336);
      this.setTooltip('Wait for a given amount of seconds.');
      this.setHelpUrl('http://www.example.com/');
    },
  };

  Blocks['random'] = {
    init: function () {
      this.appendDummyInput()
        .appendField('从')
        .appendField(new Blockly.FieldTextInput('0'), 'A')
        .appendField('到')
        .appendField(new Blockly.FieldTextInput('10'), 'B')
        .appendField('的随机数');
	  
      this.setPreviousStatement(false, null);
      this.setNextStatement(false, null);
      this.setOutput(true, 'Number');
      this.setTooltip('Use this to print to the output box.');
      this.setHelpUrl('http://www.example.com/');
      this.setColour(70);
    },
  };
  
  
  Blocks['if'] = {
    init: function () {
      this.appendDummyInput()
        .appendField('如果')
      this.appendValueInput('var');
      this.appendDummyInput()
        .appendField(':');
      this.appendStatementInput('DO')
        .appendField('');
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setColour(336);
      this.setTooltip('If Statement.');
      this.setHelpUrl('');
    },
  };

  Blocks['elif'] = {
    init: function () {
      this.appendDummyInput()
        .appendField('elif');
      this.appendValueInput('var');
      this.appendDummyInput()
        .appendField(':');
      this.appendStatementInput('DO')
        .appendField('');
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setColour(336);
      this.setTooltip('Elif Statement.');
      this.setHelpUrl('');
    },
  };

  Blocks['else'] = {
    init: function () {
      this.appendDummyInput()
        .appendField('else:');
      this.appendStatementInput('DO')
        .appendField('');
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setColour(336);
      this.setTooltip('Else statement');
      this.setHelpUrl('https://t.co/PCZC5EFe4D');
    },
  };

  Blocks['logic_compare'] = {
    init: function () {
      this.appendValueInput('A');
      this.appendDummyInput()
        .appendField(new Blockly.FieldDropdown([['大于', '>'], ['大于等于', '>='], ['小于', '<'], ['小于等于', '<='], ['等于', '=='], ['不等于', '!=']]), 'crocsigns');
      this.appendValueInput('B');
	  
      this.setPreviousStatement(false, null);
      this.setNextStatement(false, null);
      this.setOutput(true, 'Number');
      this.setTooltip('Use this to print to the output box.');
      this.setHelpUrl('http://www.example.com/');
      this.setColour(70);
    },
  };

  Blocks['logic_operation'] = {
    init: function () {
      this.appendValueInput('A');
      this.appendDummyInput()
        .appendField(new Blockly.FieldDropdown([['与', 'and'], ['或', 'or']]), 'crocsigns');
      this.appendValueInput('B');
	  
      this.setPreviousStatement(false, null);
      this.setNextStatement(false, null);
      this.setOutput(true, 'Number');
      this.setTooltip('Use this to print to the output box.');
      this.setHelpUrl('http://www.example.com/');
      this.setColour(70);
    },
  };

  Blocks['logic_negate'] = {
    init: function () {
      this.appendDummyInput()
        .appendField('非')
      this.appendValueInput('A');
	  
      this.setPreviousStatement(false, null);
      this.setNextStatement(false, null);
      this.setOutput(true, 'Number');
      this.setTooltip('Use this to print to the output box.');
      this.setHelpUrl('http://www.example.com/');
      this.setColour(70);
    },
  };

  Blocks['while_true'] = {
    init: function () {
      this.appendDummyInput()
        .appendField('重复执行:');
      this.appendStatementInput('DO')
        .appendField('');
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setColour(336);
      this.setTooltip('Forever loop.');
      this.setHelpUrl('https://t.co/PCZC5EFe4D');
    },
  };

  Blocks['whileout'] = {
    init: function () {
      this.appendDummyInput()
        .appendField('重复执行直到');
      this.appendValueInput('var');
      this.appendDummyInput()
        .appendField(':');
      this.appendStatementInput('DO')
        .appendField('');
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setColour(336);
      this.setTooltip('');
      this.setHelpUrl('http://www.example.com/');
    },
  };

  Blocks['whiletimes'] = {
    init: function () {
      this.appendDummyInput()
        .appendField('重复执行')
        .appendField(new Blockly.FieldTextInput('10'), 'var')
        .appendField('次：');
      this.appendStatementInput('DO')
        .appendField('');
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setColour(336);
      this.setTooltip('');
      this.setHelpUrl('http://www.example.com/');
    },
  };

  Blocks['for'] = {
    init: function () {
      this.appendDummyInput()
        .appendField('用')
        .appendField(new Blockly.FieldVariable('i'), 'letter')
        .appendField('来计数，从')
        .appendField(new Blockly.FieldTextInput('1'), 'var1')
        .appendField('到')
        .appendField(new Blockly.FieldTextInput('10'), 'var2')
        .appendField('间格')
        .appendField(new Blockly.FieldTextInput('1'), 'var3')
        .appendField(':');
      this.appendStatementInput('DO')
        .setCheck(null);
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setColour(336);
      this.setTooltip('');
      this.setHelpUrl('Create a for loop');
    },
  };

  Blocks['break'] = {
    init: function () {
      this.appendDummyInput()
        .appendField('终止重复');
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setColour(336);
      this.setTooltip('Pass to the next command');
      this.setHelpUrl('http://www.example.com/');
    },
  };

  Blocks['str'] = {
    init: function () {
      this.appendDummyInput()
        .appendField('str(');
      this.appendValueInput('A');
      this.appendDummyInput()
        .appendField(')');
	  
      this.setPreviousStatement(false, null);
      this.setNextStatement(false, null);
      this.setOutput(true, 'String');
      this.setTooltip('Use this to print to the output box.');
      this.setHelpUrl('http://www.example.com/');
      this.setColour(70);
    },
  };

  Blocks['pass'] = {
    init: function () {
      this.appendDummyInput()
        .appendField('跳过');
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setColour(336);
      this.setTooltip('Pass to the next command');
      this.setHelpUrl('http://www.example.com/');
    },
  };


  

  Blocks['newthread'] = {
    init: function () {
      this.appendDummyInput()
        .appendField('异步启动:');
      this.appendStatementInput('DO')
        .appendField('');
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setColour(336);
      this.setHelpUrl('https://t.co/PCZC5EFe4D');
    },
  };
  
  Blocks['gettime'] = {
    init: function () {
      this.appendDummyInput()
        .appendField('当前时间');
	  
      this.setPreviousStatement(false, null);
      this.setNextStatement(false, null);
      this.setOutput(true, 'var');
      this.setTooltip('Use this to print to the output box.');
      this.setHelpUrl('http://www.example.com/');
      this.setColour(70);
    }, 
  };
}
