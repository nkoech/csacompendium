angular
    .module('app.core')
    .constant('BASE_URL', 'http://127.0.0.1:8000/api')
    .factory('researchService', researchService);

researchService.$inject = ['$http', 'BASE_URL', '$log'];

function researchService($http, BASE_URL, $log) {
    return {
        'getListData': getListData,
        'getDetailData': getDetailData
    };

    function makeRequest(url, params) {
        var requestUrl = BASE_URL + '/' + url;
        angular.forEach(params, function(value, key){
            requestUrl = requestUrl + '?' + key + '=' + value;
        });
        return $http({
            'url': requestUrl,
            'method': 'GET',
            'headers': {
                'Content-Type': 'application/json'
            },
            'cache': true
        }).then(function(response){
            return response.data;
        }).catch(dataServiceError);
    }

    function getListData(apiNode) {
        return makeRequest(apiNode + '/', {});
    }

    function getDetailData(apiNode, id) {
        return makeRequest(apiNode + '/' + id, {});
    }

    function dataServiceError(errorResponse) {
        $log.error('XHR Failed for ShowService');
        $log.error(errorResponse);
        return errorResponse;
    }
}

