$(document).ready(function () {

    $('.person').hover(function () {
            // over
            $(this).children('.outer').addClass('on-point');
        }, function () {
            // out
            $(this).children('.outer').removeClass('on-point');
        }
    );

    $('.person').click(function () {
        let inners = $(this).children('.inner');
        console.log(inners);
        for (let index = 0; index < inners.length; index++) {
            const element = inners[index];
            console.log(element);
            $(element).toggleClass('hidden');
        }
    });

    $('.btn-get-list').click(function (e) { 
        e.preventDefault();
        let person = $(this).attr('person');
        let url = 'api/' + person + '/list';
        $.getJSON(url, function (data, textStatus, jqXHR) {
            console.log('start');
            console.log(data);
        });
    });

    $('.btn-get-one').click(function (e) {
        e.preventDefault();
        let person = $(this).attr('person');
        let id = $(this).attr('p_id');
        let url = 'api/' + person + '/' + id;
        $.getJSON(url, function (data, textStatus, jqXHR) {
                console.log('start');
                console.log(data);
        });
    });

});

