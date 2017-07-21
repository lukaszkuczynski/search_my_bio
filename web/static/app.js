$('document').ready(function(){
    $('form#api-call').submit(function(e){
        e.preventDefault();
        query = $('#query').val();
        console.log('query is '+query);
        url = 'http://localhost:5050/api/search?q='+query;
        $.get(url, function(results) {
            console.log('Response received');
            showResults(results);
        });

    });
});


function showResults(results) {

    $('#results').html('');
    $.each(results, function(index, result) {
        console.log(result);
        var tasks = result['source']['tasks'];
        var div = '<div>'+tasks+'</div>';
        $('#results').append(div)
    });

}