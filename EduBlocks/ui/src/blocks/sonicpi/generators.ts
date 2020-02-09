export default function define(Python: Blockly.BlockGenerators) {
  Python['import_sonic'] = function (block) {
    // TODO: Assemble Python into code variable.
    let code = 'from psonic import *\n';
    return code;
  };

  Python['sampleson'] = function (block) {
    let text_name = block.getFieldValue('name');
    // TODO: Assemble Python into code variable.
    let code = 'sample(' + text_name + ')\n';
    return code;
  };

  Python['play'] = function (block) {
    let text_value = block.getFieldValue('value');
    // TODO: Assemble Python into code variable.
    let code = 'play(' + text_value + ')\n';
    return code;
  };

  Python['sleep1'] = function (block) {
    let text_value = block.getFieldValue('value');
    // TODO: Assemble Python into code variable.
    let code = 'sleep(' + text_value + ')\n';
    return code;
  };

  Python['liveloop'] = function (block) {
    let branch = Blockly.Python.statementToCode(block, 'DO');
    branch = Blockly.Python.addLoopTrap(branch, block.id) ||
      Blockly.Python.PASS;
    const dropdown_num = block.getFieldValue('num');
    // TODO: Assemble Python into code variable.
    let code = '\ndef live_loop_' + dropdown_num + '():\n' + branch;
    code = code + '\nlive_thread_' + dropdown_num + '.start()\n';
    return code;
  };
}
