// document ready section

$(document).ready(function () {

    get_teacher_list();
    get_student_list();

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

    $('.show_archive_person_list').click(function (e) { 
        e.preventDefault();
        let person = $(this).attr('person');
        if (person == 'teacher') {
            get_teacher_archive_list();
        } else if (person == 'student') {
            get_student_archive_list();
        };
        $(this).addClass('active');
        $(this).siblings('.show_active_person_list').removeClass('active');
    });

    $('.show_active_person_list').click(function (e) { 
        e.preventDefault();
        let person = $(this).attr('person');
        if (person == 'teacher') {
            get_teacher_list();
        } else if (person == 'student') {
            get_student_list();
        };
        $(this).addClass('active');
        $(this).siblings('.show_archive_person_list').removeClass('active');
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

    $('.delete_person').click(function (e) { 
        e.preventDefault();
        let url = $(this).attr('url');
        let form_data = $(this).children('input').serialize();
        $.ajax({
            type: "post",
            url: url,
            data: form_data,
            success: function (response) {
                trigger_alert(alert_text=response, alert_status='alert-success', delay=2000);
                setTimeout(() => {
                    location.href = "/";
                }, (delay+1000));
            }
        });
    });

    $('.archive_person').click(function (e) { 
        e.preventDefault();
        let url = $(this).attr('url');
        let form_data = $(this).children('input').serialize();
        $.ajax({
            type: "post",
            url: url,
            data: form_data,
            success: function (response) {
                trigger_alert(alert_text=response, alert_status='alert-success', delay=2000);
                setTimeout(() => {
                    location.reload();;
                }, 2000);
            }
        });
    });

    // how to use jq on dinamic objects
    // $('#add_person_body').on('click', '#add_teacher_btn', function () {
    //     console.log('click');
    // });

});

// end of document ready section

// functions section

// teachers

function get_teacher_list() {
    $.get("/teacher/list/", function (data, textStatus, jqXHR) {
            $('.teacher_list').html(data);
        },
        "html"
    );
};

function get_teacher_archive_list() {
    $.get("/teacher/list/archive/", function (data, textStatus, jqXHR) {
            $('.teacher_list').html(data);
        },
        "html"
    );
};

function add_teacher() {
    let form_data = $('#add_teacher_form').serialize();
    $.ajax({
        type: "post",
        url: "/teacher/add/",
        data: form_data,
        success: function (response) {
            $('#add_person_modal').modal('toggle');
            get_teacher_list();
            trigger_alert(alert_text=response, alert_status='alert-success', delay=2000);
        },
        error : function (response) {
            $('#add_person_body').html(response.responseText);
        }
    });
};

// students

function get_student_list() {
    $.get("/student/list/", function (data, textStatus, jqXHR) {
            $('.student_list').html(data);
        },
        "html"
    );
};

function get_student_archive_list() {
    $.get("/student/list/archive", function (data, textStatus, jqXHR) {
            $('.student_list').html(data);
        },
        "html"
    );
};

function add_student(params) {
    let form_data = $('#add_student_form').serialize();
    $.ajax({
        type: "post",
        url: "/student/add/",
        data: form_data,
        success: function (response) {
            $('#add_person_modal').modal('toggle');
            get_student_list();
            trigger_alert(alert_text=response, alert_status='alert-success', delay=2000);
        },
        error: function (response) {
            $('#add_person_body').html(response.responseText);
        }
    });
};

// alerts

function trigger_alert(alert_text, alert_status, delay) {
    show_alert(alert_text=alert_text, alert_status=alert_status);
    setTimeout(() => {
        hide_alert();
    }, delay);
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

// end of functin section