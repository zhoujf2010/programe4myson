export default function define(Python: Blockly.BlockGenerators) {
  Python['connect'] = function (block) {
    Blockly.Python.definitions_['import_wedo'] = 'from legolib import wedo';
    var code = 'hub = wedo()\n';
    return code;
  };

  Python['motoron'] = function (block) {
    const text_const = Blockly.Python.valueToCode(block, 'val', 0) || "100";
    var code = 'hub.turn_motor(' + text_const + ')\n';
    return code;
  };

  Python['motoroff'] = function (block) {
    // TODO: Assemble Python into code variable.
    var code = 'hub.motor_brake()\n';
    return code;
  };

  Python['disconnect'] = function (block) {
    // TODO: Assemble Python into code variable.
    var code = 'hub.disconnect()\n';
    return code;
  };

  Python['distnace'] = function (block) {
    const text_const = "hub.get_object_distance()";
    return [text_const, 0];
  };

  Python['tiltX'] = function (block) {
    const text_const = "hub.get_tiltX()";
    return [text_const, 0];
  };

  Python['tiltY'] = function (block) {
    const text_const = "hub.get_tiltY()";
    return [text_const, 0];
  };

  Python['ev3connect'] = function (block) {
    Blockly.Python.definitions_['import_ev3'] = 'from legolib import ev3';
    var code = 'ev3 = ev3()\n';
    return code;
  };

  Python['ev3disconnect'] = function (block) {
    var code = 'ev3.disconnect()\n';
    return code;
  };

  Python['ev3motoron'] = function (block) {
    var port =block.getFieldValue('port');
    const text_const = Blockly.Python.valueToCode(block, 'val', 0) || "100";
    var code = 'ev3.MotorOn(ev3.PORT_' + port +', ' + text_const + ')\n';
    return code;
  };

  Python['ev3motordegree'] = function (block) {
    var port =block.getFieldValue('port');
    const degree = Blockly.Python.valueToCode(block, 'degree', 0) || "90";
    const text_const = Blockly.Python.valueToCode(block, 'val', 0) || "100";
    var code = 'ev3.MotorOndegrees(ev3.PORT_' + port +', ' + text_const + ',' + degree + ')\n';
    return code;
  };

  Python['ev3motorpos'] = function (block) {
    var port =block.getFieldValue('port');
    var code = 'ev3.MotorPosition(ev3.PORT_' + port +')';
    return [code,0];
  };

  Python['ev3motoroff'] = function (block) {
    var port =block.getFieldValue('port');
    var brake =block.getFieldValue('brake');
    if (brake =="TRUE")
      brake = "True"
    else
      brake = "False"

    var code = 'ev3.MotorOff(ev3.PORT_' + port +',' + brake + ')\n';
    return code;
  };

  Python['ev3ultradistance'] = function (block) {
    var port =block.getFieldValue('port');
    var code = 'ev3.Ultrasonic_distance(ev3.PORT_' + port +')';
    return [code,0];
  };

  Python['ev3touchispressed'] = function (block) {
    var port =block.getFieldValue('port');
    var code = 'ev3.Touch_ispressed(ev3.PORT_' + port +')';
    return [code,0];
  };

  Python['ev3touchwaitpressed'] = function (block) {
    var port =block.getFieldValue('port');
    var code = 'ev3.Touch_wait4pressed(ev3.PORT_' + port +')\n';
    return code;
  };

  Python['ev3touchwaitreleased'] = function (block) {
    var port =block.getFieldValue('port');
    var code = 'ev3.Touch_wait4released(ev3.PORT_' + port +')\n';
    return code;
  };

  Python['ev3colorambient'] = function (block) {
    var port =block.getFieldValue('port');
    var code = 'ev3.color_ambient(ev3.PORT_' + port +')';
    return [code,0];
  };

  Python['ev3colorreflected'] = function (block) {
    var port =block.getFieldValue('port');
    var code = 'ev3.color_reflected(ev3.PORT_' + port +')';
    return [code,0];
  };

  Python['ev3colordetect'] = function (block) {
    var port =block.getFieldValue('port');
    var code = 'ev3.color_detect(ev3.PORT_' + port +')';
    return [code,0];
  };

  Python['ev3colordetect2'] = function (block) {
    var port =block.getFieldValue('port');
    var code = 'ev3.getColName(ev3.color_detect(ev3.PORT_' + port +'))';
    return [code,0];
  };

  Python['ev3gyroangle'] = function (block) {
    var port =block.getFieldValue('port');
    var code = 'ev3.Gyro_angle(ev3.PORT_' + port +')';
    return [code,0];
  };

  Python['ev3gyrorate'] = function (block) {
    var port =block.getFieldValue('port');
    var code = 'ev3.Gyro_rate(ev3.PORT_' + port +')';
    return [code,0];
  };

  Python['ev3playsoundfile'] = function (block) {
    var filename =block.getFieldValue('filename');
    var sound =block.getFieldValue('sound');
    var code = 'ev3.playSoundFile("' + filename +'",' + sound + ')\n';
    return code;
  };

  Python['ev3displayimage'] = function (block) {
    var filename =block.getFieldValue('filename');
    var code = 'ev3.displayImage("' + filename +'")\n';
    return code;
  };
}
