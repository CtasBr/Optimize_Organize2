$('.input-file input[type=file]').on('change', function () {
    let file = this.files[0];
    console.log(file);
    $(this).next().html(file.name);
});