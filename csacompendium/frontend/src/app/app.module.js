require('angular');
import '../assets/css/main.scss';
import '../users.html';
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
