$(document).ready(function () {
  $('li.active').removeClass('active').removeAttr('aria-current');
  $('a.active').removeClass('active').removeAttr('aria-current');
  $('a[href="' + location.pathname + '"]').closest('li').addClass('active').attr('aria-current', 'page');
  $('a[href="' + location.pathname + '"]').addClass('active');
});
