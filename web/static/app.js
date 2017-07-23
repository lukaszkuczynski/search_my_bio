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

function create_card_html(header, title, body, tags) {
    html = '';
    html += '<div class="card">';
    html +=     '<div class="card-header">' + header + "</div>";
    html +=     '<div class="card-block">';
    html +=         '<h4 class="card-title">' + title + "</h4>";
    html +=         '<div class="card-text">' + body + "</div>";
    html +=     '</div>'
    html +=     '<div class="card-footer">' + tags + "</div>"
    html += '</div>';
    return html;
}

function showResults(results) {

    $('#results').html('');
    $.each(results, function(index, result) {
        console.log(result);
        var tasks = result['source']['tasks'];
        var title = result['source']['title'] || 'Title';
        var description = result['source']['description'];
        var tags = result['source']['technologies'];
        var card_html = create_card_html('Commercial', title, description, tags);
        $('#results').append(card_html)
    });

}