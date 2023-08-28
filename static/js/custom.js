$(document).ready(function () {

    $('.date_in_calendar').click(function (e) { 
        e.preventDefault();
        let teacher_id = $(this).attr('teacher');
        let year = $(this).attr('year');
        let month = $(this).attr('month');
        let day = $(this).attr('day');
        let url = `/teacher/${teacher_id}/${year}/${month}/${day}/`;
        $.get(url, function (data, textStatus, jqXHR) {
                $('#classes_per_day').html(data);
            },
            "html"
        );
    });

    $('.add_person').click(function (e) { 
        e.preventDefault();
        let person = $(this).attr('person');
        let url = `/${person}/add/`
        if (person == 'teacher') {
            $("#add_person_title").text('Добавить преподавателя');
        } else if (person == 'student') {
            $('#add_person_title').text('Добавить студента');
        };
        $.get(url, function (data, textStatus, jqXHR) {
                $('#add_person_body').html(data);
                $('#add_person_modal').modal('toggle');
            },
            "html"
        );
    });

    // how to use jq on dinamic objects
    // $('#add_person_body').on('click', '#add_teacher_btn', function () {
    //     console.log('click');
    // });

});

function add_person() {
    let form_data = $('#add_person_form').serialize();
    $.ajax({
        type: "post",
        url: "/teacher/add/",
        data: form_data,
        success: function (response) {
            $('#add_person_modal').modal('toggle');
            show_alert(alert_text=response, alert_status='alert-success');
            console.log('show');
            setTimeout(() => {
                hide_alert();
            }, 3000);
            console.log('hide');
        },
        error : function (response) {
            $('#add_person_body').html(response.responseText);
        }
    });
};

function show_alert(alert_text, alert_status) {
    const alert_body = `<div class="alert ${alert_status}" id="alert_content" role="alert">
                            <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                            <p id="add_person_status">${alert_text}</p>
                        </div>`;
    $('#alert_block').html(alert_body);
};

function hide_alert() {
    $('#alert_content').alert('close');
};