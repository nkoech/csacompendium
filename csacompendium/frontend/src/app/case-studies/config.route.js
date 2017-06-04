angular
    .module('app.case-studies')
    .config(routes);

function routes($routeProvider, $locationProvider) {
    $routeProvider.
        when('/case-studies', {
            title: 'Case Studies',
            controller: 'CaseStudiesController',
            controllerAs: 'vm',
            templateUrl: require("./case-studies.tpl.html")
        });
    $locationProvider.html5Mode(true);
}