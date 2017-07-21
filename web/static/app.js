$('document').ready(function(){
    $('form#api-call').submit(function(e){
        e.preventDefault();
        query = $('#query').val();
        console.log('query is '+query);
        url = 'http://localhost:5050/api/search?q='+query;
        $.get(url, function(results) {
            console.log('Response received');
            console.log(results);
            $.each(results, function(index, result) {
                console.log(result['source']['tasks']);
            });
        });

    });
});