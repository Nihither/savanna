$(document).ready(function () {

    // $('.person').hover(function () {
    //         // over
    //         $(this).children('.outer').addClass('on-point');
    //     }, function () {
    //         // out
    //         $(this).children('.outer').removeClass('on-point');
    //     }
    // );

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

    $('.modalClose').click(function (e) { 
        e.preventDefault();
        $('.modalBack').css('display', 'none');
    });

    $('.btn-modal-open').click(function (e) { 
        e.preventDefault();
        let person = $(this).attr('person');
        let person_id = $(this).attr('person_id');
        let url = person + '/' + person_id + '/details';
        console.log(url);
        $.get(url, function (data, textStatus, jqXHR) {
                $('.modalWindow').html(data);
            },
            "html"
        );
        $('.modalBack').css('display', 'block');
    });

});

