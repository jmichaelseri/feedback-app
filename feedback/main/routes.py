from flask import(
    Flask, render_template,
    request, redirect,
    url_for, flash
)
from feedback.main.forms import FeedbackForm
from feedback.models import Feedback
from feedback.main import bp
from feedback import db

@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
def index():
    form = FeedbackForm()
    if form.validate_on_submit():
        name = form.name.data
        service = form.service.data
        rating = form.rating.data
        comment = form.comment.data

        if Feedback.query\
            .filter(Feedback.name == name)\
            .count() == 0:
            feedback = Feedback(
                name=name,
                service=service,
                rating=rating,
                comment=comment
            )
            db.session.add(feedback)
            db.session.commit()
        else:
            flash('You have already rated our services!')
            return redirect(url_for('main.index'))
        return redirect(url_for('main.success'))
    return render_template('feedback/index.html', form=form)


@bp.route('/success', methods=['GET', 'POST'])
def success():
    return render_template('feedback/success.html')
