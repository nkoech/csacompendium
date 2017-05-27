export default angular
    .module('app.layout')
    .controller('Collapse', Collapse);

function Collapse() {
    var vm = this;
    vm.isNavCollapsed = true;
}
