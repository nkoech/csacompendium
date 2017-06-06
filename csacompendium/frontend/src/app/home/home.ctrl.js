angular
    .module('app.home')
    .controller('HomeController', HomeController);

HomeController.$inject = ['researchService'];

function HomeController(researchService) {
    var vm = this;
    vm.query = function(apiNode, query){
        vm.data = researchService.search(apiNode, query);
        console.log(vm.data);
    };

    vm.query('indicatoroutcome/researchoutcomeindicator', {});
}