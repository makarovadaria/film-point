

function submitSurvey() {
    // Create a custom notification element
    const notification = document.createElement('div');
    notification.classList.add('custom-notification');
    notification.innerHTML = "Survey submitted!<br><br>Ready for your movie recommendations?";

    // Append the notification to the body
    document.body.appendChild(notification);

    // Remove the notification after a delay and redirect
    setTimeout(() => {
      notification.remove();
      window.location.href = 'movie_survey_result.html';
    }, 3000); // Adjust delay as needed
  }

  // Add event listeners to buttons
  document.addEventListener('DOMContentLoaded', () => {
    const buttons = document.querySelectorAll('.button-53');
    if (buttons.length > 0 && window.location.pathname.includes('movie_survey3.html')) {
      buttons.forEach(button => {
        button.addEventListener('click', submitSurvey);
      });
    }
  });

