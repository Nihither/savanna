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

});

