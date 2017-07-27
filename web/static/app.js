$('document').ready(function(){
    $('form#api-call').submit(function(e){
        e.preventDefault();
        query = $('#query').val();
        console.log('query is '+query);
        url = '/api/search?q='+query;
        $.get(url, function(results) {
            console.log('Response received');
            showResults(results);
        })
        .fail(function() {
            alert( "error" );
        })

    });
});

function create_card_html(header, context) {
    html = '';
    html += '<div class="card" style="margin-bottom:30px">';
    html +=     '<div class="card-header">' + header + "</div>";
    html +=     '<div class="card-block">';
    html +=         '<h4 class="card-title">' + context['title'] + "</h4>";
    html +=         '<div class="card-text">';
    html +=             '<p>'+  context['description'] + "</p>";
    if (context['challenges']) {
        html +=             '<p>Challenges:<ul>';
        for (i=0; i<context['challenges'].length; i++) {
            var challenge = context['challenges'][i];
            html +=             '<li>'+challenge+'</li>';
        }
        html +=             '</ul></p>';
    }
    if (context['learned']) {
        html +=             '<p>Lessons learned:<ul>';
        for (i=0; i<context['learned'].length; i++) {
            var lesson = context['learned'][i];
            html +=             '<li>'+lesson+'</li>';
        }
        html +=             '</ul></p>';
    }
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
            "time" : result['source']['started'],
            "learned" : result['source']['learned'],
            "challenges" : result['source']['challenges']
        }
        commercial_or_private = result['source']['type']
        var card_html = create_card_html(commercial_or_private, context);
        $('#results').append(card_html)
    });

}