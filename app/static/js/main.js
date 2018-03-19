// Dropzone Error Flashing
function flashError(message) {
    $('.dz-message').show();
    $('.dz-error-message').text(message);
    $('.dz-preview').hide();
    console.log(message);
}


// Dropzone configuration options
Dropzone.options.audioForm = {
    previewTemplate: `
        <div class="dz-preview dz-file-preview">
            <div class="dz-details">
                <div class="dz-filename"><span data-dz-name></span></div>
                <div class="dz-size" data-dz-size></div>
            </div>
            <button type="button" id="btn-upload" class="btn btn-primary">Begin Upload</button>
        </div>
    `,
    maxFilesize: 30,
    createImageThumbnails: false,
    autoProcessQueue: false,
    parallelUploads: 1,
    acceptedFiles: ".m4a, .mp3, .wav, .wma, .ogg",
    init: function() {
        var dropz = this;

        dropz.on("addedfile", function(file) {
            // Only allow single file upload. Old files are replaced with new ones.
            if (dropz.files[1]!=null){
                dropz.removeFile(dropz.files[0]);
            }
            $('.dz-message').hide();
            // Hook up the start button
            $('#btn-upload').click(function( event ) {
                event.preventDefault();
                dropz.processQueue(file);
            });
        });

        dropz.on("sending", function(file) {
            $('.dropzone').fadeOut();
            $('body').toggleClass('loaded');
        });

        dropz.on("error", function(file, errorMessage) {
            // Reset on error
            $('.dropzone').show();
            $('.dz-message').show();
            flashError(errorMessage);
        });

        dropz.on("success", function(file, data) {
            if (data.success) {
                // Move to the next screen
                console.log('Successfully uploaded file: ' + data.filename);
                $(".container").html(data.content);
                $('body').toggleClass('loaded');
            } else {
                // There was an error
                flashError(data.error);
                $('body').toggleClass('loaded');
            }
        });
    }
};
