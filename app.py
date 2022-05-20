from flask import Flask, render_template
import utils
app = Flask(__name__)


@app.route('/')
def page_all_candidates_from_json():
    candidates = utils.load_candidates_from_json()
    return render_template('list.html', candidates=candidates)


@app.route('/candidate/<int:pk>')
def page_candidate_by_pk(pk):
    candidate = utils.get_candidate(pk)
    return render_template('single.html', candidate=candidate)


@app.route('/skill/<string:skill_name>')
def page_candidates_by_skill(skill_name):
    candidates = utils.get_candidates_by_skill(skill_name)
    counter = len(candidates)
    return render_template('skill.html', candidates=candidates, counter=counter, skill=skill_name)

@app.route('/search/<candidate_name>')
def page_candidates_by_name(candidate_name):
    candidates = utils.get_candidates_by_name(candidate_name)
    counter = len(candidates)
    return render_template('search.html', candidates=candidates, counter=counter, candidate_name=candidate_name)


app.run()