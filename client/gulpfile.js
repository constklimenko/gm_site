var gulp = require('gulp');

var less = require('gulp-less');
var authoprefixer = require('gulp-autoprefixer');
var concat = require('gulp-concat');
var sourcemaps = require('gulp-sourcemaps');
var cleanCss = require('gulp-clean-css');
var browserSync = require('browser-sync').create();

var config = {
    path: {
        less: 'src/less/*.less',
        // html: 'static/index.html',

    },
    output: {
        cssName: 'index.css',
        path: '../gm_site/static/css',
        path_file: 'land3/public/l3-index.html',
        path_file_css: 'static/css/index.css',

    }
}

gulp.task('less', function() {
    return gulp.src(config.path.less)
        .pipe(sourcemaps.init())
        .pipe(less())
        .pipe(concat(config.output.cssName))
        .pipe(authoprefixer())
        // .pipe(cleanCss())
        .pipe(sourcemaps.write())
        .pipe(gulp.dest(config.output.path));
    // .pipe(browserSync.stream());
});

gulp.task('serve', (done) => {

    gulp.watch(config.path.less, gulp.series('less'));

    done();
});

gulp.task('default', gulp.series('less'));