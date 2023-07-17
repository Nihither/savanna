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
        let url = "api/student/list";
        $.getJSON(url, function (data, textStatus, jqXHR) {
            alert('start');
            console.log(data);
        });
    });

    $('.btn-get-one').click(function (e) { 
        console.log('button was clicked');
        e.preventDefault();
        // let id = $(this).attr('p_id');
        let id = 4;
        let url = 'api/student/' + id;
        $.getJSON(url, function (data, textStatus, jqXHR) {
                console.log('start');
                console.log(data);
        });
    });

});

