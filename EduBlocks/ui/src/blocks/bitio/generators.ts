export default function define(Python: Blockly.BlockGenerators) {
  Python['importmb'] = function (block) {
    // TODO: Assemble Python into code variable.
    var code = 'import microbit\n';
    return code;
  };

  Python['displayscrolltext'] = function (block) {
    var text_message = block.getFieldValue('message');
    // TODO: Assemble Python into code variable.
    var code = 'microbit.display.scroll("' + text_message + '")\n';
    return code;
  };

  Python['displayscrollvar'] = function (block) {
    var text_varmess = block.getFieldValue('varmess');
    // TODO: Assemble Python into code variable.
    var code = 'microbit.display.scroll(' + text_varmess + ')\n';
    return code;
  };

  Python['microsleep'] = function (block) {
    var text_time = block.getFieldValue('time');
    // TODO: Assemble Python into code variable.
    var code = 'microbit.sleep(' + text_time + ')\n';
    return code;
  };

  Python['displayshow'] = function (block) {
    var text_show = block.getFieldValue('show');
    // TODO: Assemble Python into code variable.
    var code = 'microbit.display.show(' + text_show + ')\n';
    return code;
  };

  Python['displayclear'] = function (block) {
    // var text_show = block.getFieldValue('show');
    // TODO: Assemble Python into code variable.
    var code = 'microbit.display.clear()\n';
    return code;
  };
}
