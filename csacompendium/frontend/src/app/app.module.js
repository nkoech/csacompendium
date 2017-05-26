// require('bootstrap-css-only');
// require('font-awesome');
// import '../../node_modules/bootstrap-css-only/css/bootstrap.min.css'
// import '../../node_modules/font-awesome/css/font-awesome.min.css'
import '../assets/css/main.css';
import '../test_users.html';
import '../test_index.html';
require('angular');
require('angular-ui-bootstrap');
import { RandomGenerator } from './random-generator';
const outputParagraph = $('#outputParagraph');

const outputRandomInt = () => {
    outputParagraph.html(RandomGenerator.randomInteger());
};

const outputRandomRange = () => {
    outputParagraph.html(RandomGenerator.randomRange(1, 500));
};

const buttonRndInt = $('#randomInt');
const buttonRndRange = $('#randomRange');

buttonRndInt.click(outputRandomInt);
buttonRndRange.click(outputRandomRange);
