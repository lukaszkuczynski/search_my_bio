$('document').ready(function(){
    $('form#api-call').submit(function(e){
        e.preventDefault();
        query = $('#query').val();
        console.log('query is '+query);
        url = '/api/search?q='+query;
        $.get(url, function(response) {
            console.log('Response received');
            console.log(response);
            hits = response['hits']['hits']
            if (hits.length > 0) {
                showHits(hits);
            } else {
                showWarning('No results found for query <strong>'+query+'</strong>')
            }
            showProcessingTime("took " + response['took'] + " ms")
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

function showHits(hits) {
    $('#noresults').hide();
    $('#results').html('');
    $.each(hits, function(index, hit) {
        console.log(hit);
        context = {
            "tasks" : hit['_source']['tasks'],
            "title" : hit['_id'],
            "description" : hit['_source']['description'],
            "tags" : hit['_source']['technologies'],
            "time" : hit['_source']['started'],
            "learned" : hit['_source']['learned'],
            "challenges" : hit['_source']['challenges']
        }
        commercial_or_private = hit['_source']['type']
        var card_html = create_card_html(commercial_or_private, context);
        $('#results').append(card_html)
    });

}

function showWarning(text) {
    $('#results').html('');
    $('#noresults').show();
    $('#noresults').html(text);
}

function showProcessingTime(time) {
    $('#took').html(time)
}