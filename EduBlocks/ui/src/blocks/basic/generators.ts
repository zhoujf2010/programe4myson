export default function define(Python: Blockly.BlockGenerators) {
  //https://blockly-demo.appspot.com/static/demos/code/index.html

  Python['const_value'] = function (block) {
    const text_const = block.getFieldValue('var') || "";
    return [text_const, 0];
  };

  Python['const_txt'] = function (block) {
    const text_const = "'" + block.getFieldValue('var') + "'";
    return [text_const, 0];
  };


  Python['basic_print'] = function (block) {
    let text_print2 = Blockly.Python.valueToCode(block, 'VALUE', Blockly.Python.ORDER_NONE);
    const code = 'print(' + text_print2 + ')\n';
    return code;
  };

  Python['basic_input'] = function (block) {
    const text_const = block.getFieldValue('var') || "";
    const code = 'input(\'' + text_const + '\')';
    return [code, 0];
  };

  Python['math_arithmetic'] = function (block) {
    var operator = block.getFieldValue('crocsigns');
    var order = 5;
    if (operator == '+' || operator == '-')
      order = 6;
    if (operator == '*' || operator == '/' || operator == '%')
      order = 5;
    if (operator == '^')
      order = 3;

    var argument0 = Blockly.Python.valueToCode(block, 'A', order) || '0';
    var argument1 = Blockly.Python.valueToCode(block, 'B', order) || '0';
    var code = argument0 + ' ' + operator + ' ' + argument1;
    return [code, order];
  };

  Python['math_single'] = function (block) {
    var operator = block.getFieldValue('crocsigns');
    var order = 5;
    var argument1 = Blockly.Python.valueToCode(block, 'A', order) || '0';
    var code = operator + argument1;
    return [code, order];
  };

  Python['sleep'] = function (block) {
    Blockly.Python.definitions_['import_time'] = 'import time';
    var text_sleeptime = Blockly.Python.valueToCode(block, 'sleepTime', 0) || '1';
    const code = 'time.sleep(' + text_sleeptime + ')\n';
    return code;
  };

  Python['random'] = function (block) {
    Blockly.Python.definitions_['import_random'] = 'import random';
    const argument0 = block.getFieldValue('A') || "0";
    const argument1 = block.getFieldValue('B') || "10";
    var code = 'random.randint(' + argument0 + ',' + argument1 + ')';
    return [code, 0];
  };


  Python['if'] = function (block) {
    var text_const = Blockly.Python.valueToCode(block, 'var', 0) || 'True';
    let branch = Blockly.Python.statementToCode(block, 'DO');
    branch = Blockly.Python.addLoopTrap(branch, block.id) || Blockly.Python.PASS;
    return 'if ' + text_const + ':\n' + branch;
  };

  Python['elif'] = function (block) {
    var text_const = Blockly.Python.valueToCode(block, 'var', 0) || 'True';
    let branch = Blockly.Python.statementToCode(block, 'DO');
    branch = Blockly.Python.addLoopTrap(branch, block.id) || Blockly.Python.PASS;
    return 'elif ' + text_const + ':\n' + branch;
  };

  Python['else'] = function (block) {
    let branch = Blockly.Python.statementToCode(block, 'DO');
    branch = Blockly.Python.addLoopTrap(branch, block.id) || Blockly.Python.PASS;
    return 'else:\n' + branch;
  };

  Python['logic_compare'] = function (block) {
    var operator = block.getFieldValue('crocsigns');
    var order = 5;

    var argument0 = Blockly.Python.valueToCode(block, 'A', order) || '0';
    var argument1 = Blockly.Python.valueToCode(block, 'B', order) || '0';
    var code = argument0 + ' ' + operator + ' ' + argument1;
    return [code, order];
  };

  Python['logic_operation'] = function (block) {
    var operator = block.getFieldValue('crocsigns');
    var order = 6;

    var argument0 = Blockly.Python.valueToCode(block, 'A', order) || '0';
    var argument1 = Blockly.Python.valueToCode(block, 'B', order) || '0';
    var code = argument0 + ' ' + operator + ' ' + argument1;
    return [code, order];
  };

  Python['logic_negate'] = function (block) {
    var order = 3;
    var argument1 = Blockly.Python.valueToCode(block, 'A', order) || 'True';
    var code = "!" + argument1;
    return [code, order];
  };

  Python['while_true'] = function (block) {
    let branch = Blockly.Python.statementToCode(block, 'DO');
    branch = Blockly.Python.addLoopTrap(branch, block.id) || Blockly.Python.PASS;
    return 'while True:\n' + branch;
  };

  Python['whileout'] = function (block) {
    var text_1 = Blockly.Python.valueToCode(block, 'var', 0) || 'True';
    let branch = Blockly.Python.statementToCode(block, 'DO');
    branch = Blockly.Python.addLoopTrap(branch, block.id) || Blockly.Python.PASS;
    const code = 'while ' + text_1 + ':\n' + branch;
    return code;
  };

  Python['whiletimes'] = function (block) {
    const text_const = block.getFieldValue('var') || "";
    let branch = Blockly.Python.statementToCode(block, 'DO');
    branch = Blockly.Python.addLoopTrap(branch, block.id) || Blockly.Python.PASS;
    const code = 'for count in range(' + text_const + '):\n' + branch;
    return code;
  };

  Python['for'] = function (block) {
    let branch = Blockly.Python.statementToCode(block, 'DO');
    branch = Blockly.Python.addLoopTrap(branch, block.id) || Blockly.Python.PASS;
    var text_letter = Blockly.Python.variableDB_.getName(block.getFieldValue('letter'), Blockly.Variables.NAME_TYPE);
    const var1 = block.getFieldValue('var1');
    const var2 = block.getFieldValue('var2');
    const var3 = block.getFieldValue('var3');
    let code = 'for ' + text_letter + ' in range(' + var1 + ',' + var2 + ',' + var3 + '):\n' + branch;
    if (var3 == "1")
      code = 'for ' + text_letter + ' in range(' + var1 + ',' + var2 + '):\n' + branch;
    return code;
  };

  Python['break'] = function (block) {
    const code = 'break \n';
    return code;
  };

  Python['pass'] = function (block) {
    const code = 'pass \n';
    return code;
  };

  Python['str'] = function (block) {
    var argument0 = Blockly.Python.valueToCode(block, 'A',0) ;
    var code = 'str(' + argument0 + ')';
    return [code, 0];
  };

  Python['newthread'] = function (block) {
    let branch = Blockly.Python.statementToCode(block, 'DO');
    branch = Blockly.Python.addLoopTrap(branch, block.id) || Blockly.Python.PASS;
    var argstr = '()'
    if (branch.indexOf('(') > 0) {
      argstr = branch.substr(branch.indexOf('(')).trim();
      branch = branch.substr(0, branch.indexOf('(')).trim();
    }
    return 'Thread(target=' + branch + ',args=' + argstr + ').start()\n';
  };

  Python['gettime'] = function (block) {
    Blockly.Python.definitions_['import_wedo'] = 'import time';
    const text_const = "time.time()";
    return [text_const, 0];
  };
}
