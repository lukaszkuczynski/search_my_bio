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

function create_card_html(header, context) {
    html = '';
    html += '<div class="card" style="margin-bottom:30px">';
    html +=     '<div class="card-header">' + header + "</div>";
    html +=     '<div class="card-block">';
    html +=         '<h4 class="card-title">' + context['title'] + "</h4>";
    html +=         '<div class="card-text">';
    html +=             '<p>'+  context['body'] + "</p>";
    if (context['tags']) {
        html +=             '<p>';
        for (i=0; i<context['tags'].length; i++) {
            html +=             '<span class="badge badge-default" style="margin-right: 10px">'+ context['tags'][i] + "</span>"
        }
        html +=             '</p>'
    }
    html +=          "</div>";
    html +=     '</div>'
    html +=     '<div class="card-footer text-muted"> started at ' + context['time'] + "</div>"
    html += '</div>';
    return html;
}

function showResults(results) {

    $('#results').html('');
    $.each(results, function(index, result) {
        console.log(result);
        context = {
            "tasks" : result['source']['tasks'],
            "title" : result['id'],
            "description" : result['source']['description'],
            "tags" : result['source']['technologies'],
            "time" : result['source']['started']
        }
        var card_html = create_card_html('Commercial', context);
        $('#results').append(card_html)
    });

}