import path = require('path');
import changeCase = require('change-case');

const includeFolder = require('include-folder');
const samples: { [file: string]: string } = includeFolder(path.join(__dirname, '..', 'samples'));

const Samples: { [name: string]: string } = {};

Object.keys(samples).forEach((file) => {
  Samples[changeCase.titleCase(file)] = samples[file];
});

function newSamples() {
  function getSamples() {
    return Object.keys(Samples);
  }

  function getSample(file: string) {
    return Samples[file];
  }

  return {
    getSamples,
    getSample,
  };
}

export {
  newSamples,
};
