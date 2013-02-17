# Create your views here.

from django.template import Context, loader
from django.http import HttpResponse

#
# TECHNICAL WRITING
#

def carpentry_gallery(request):
    t = loader.get_template('gallery.html')
    c = Context({
    	'background_color': '000040',
    	'link_color': 'E18700',
    	'gallery_path': 'technical/carpentry',
    	'copyright_owner': "ABU",
    	'gallery_title': "Work for Las Vegas Carpenter's Union",
    	'gallery_list': [{
    	    'filename_stem': 'carpentry-cover',
    		'summary': 'Technical Manuals for Carpenters',
    		'blurb': "I was hired to gather information from domain experts and written sources and write several 120 to 150-page handbooks for the <a href='http://carpenters.org'>United Brotherhood of Carpenters and Joiners of America</a>. This gallery shows representative samples from one of those works, on topics in Timber Construction."
    	},{
    	    'filename_stem': 'carpentry-6',
    		'summary': 'Information from Multiple Sources',
    		'blurb': "My job was to consult with domain experts, source information from printed materials, and create and/or refine a presentation of the information that carpentry apprentices could use. I provided the deliverables to graphic designers and proofread the result before publication."
    	},{
    	    'filename_stem': 'carpentry-22',
    		'summary': 'Review Questions and Callouts',
    		'blurb': "I also included review questions in the projects and callouts in the text for particularly important points."
    	},{
    	    'filename_stem': 'carpentry-44',
    		'summary': 'Diverse Subject Matter',
    		'blurb': "I needed to survey a wide variety of topics in construction. Beyond interpreting mechanical diagrams, the manuals required fact-checking on materials, insects, compliance, and more."
    	},{
    	    'filename_stem': 'carpentry-69',
    		'summary': 'Definitions and Diagrams',
    		'blurb': "Though I did not draw any of the diagrams for the book, it was necessary to pull and sort diagrams and determine which ones could be used 'as-is' and which would need to be redrawn by a contractor."
    	},{
    	    'filename_stem': 'carpentry-112',
    		'summary': 'Step-by-Step Instructions',
    		'blurb': "Another aspect of the project was to write clear procedures, which I later did a lot more of as a writer for <a href='http://ehow.com'>ehow.com</a> and <a href='http://business.com'>business.com</a>."
    	},{
    	    'filename_stem': 'carpentry-119',
    		'summary': 'Glossary and Index',
    		'blurb': "The glossaries and indexes were built using keywords chosen by the domain experts, who were also teachers of these classes."
    	},{
    	    'filename_stem': 'carpentry-back',
    		'summary': 'In Conclusion',
    		'blurb': "Writing carpentry manuals was a good experience. Though I had no prior experience in the domain, as a technical writer I was able to sort through the information and work with domain experts, project managers, and other team members as needed.  <a href='http://meredithmcghan.com'>Back to Main Site</a>"
    	}]
    })
    return HttpResponse(t.render(c))

#
# JOURNALISM
#

def cover_stories_gallery(request):
    t = loader.get_template('gallery.html')
    c = Context({
    	'background_color': '3c4c43',
    	'link_color': 'f7ce90',
    	'gallery_path': 'journalism/cover-stories',
    	'copyright_owner': 'Las Vegas CityLife',
    	'gallery_title': 'Las Vegas CityLife Cover Stories',
    	'gallery_list': [{
    		'filename_stem': 'homeless-cover',
    		'summary': 'Writing for CityLife',
    		'blurb': "<a href='http://lasvegascitylife.com/'>Las Vegas <i>CityLife</i></a> is the oldest of three alternative weekly newspapers in the Las Vegas Valley.  Despite publishing a paper every week, the pace was surprisingly manageable.  My responsibilities included maintaining event listings, writing news and arts stories, and copyediting.  Here I've excerpted the stories I worked on that made the cover."
    	},{
    	    'filename_stem': 'homeless-1',
    		'summary': 'Genesis of the Idea',
    		'blurb': "This was my first cover story for <i>CityLife</i>, after getting hired as a full-time staff member. The small neighboring city of Henderson had a sizeable homeless population. My editor asked me to delve into the problem and see how bad it was."
    	},{
    	    'filename_stem': 'homeless-2',
    		'summary': 'The Questions',
    		'blurb': "How many homeless people lived in Henderson and how did the city help them? I visited the Salvation Army there and found subjects for ad-hoc 'man on the street' interviews. Over the two weeks I had to write the story, I also interviewed homeless advocates and social service providers regarding local resources."
    	},{
    	    'filename_stem': 'homeless-3',
    		'summary': 'Being in the Trenches',
    		'blurb': "My natural empathy makes it easy for me to work with interviewing the homeless, or <a href='http://meredithmcghan.com/media/documents/voting-restoration-nevada-2008.pdf'>helping ex-felons reconnect with society</a>. I was glad to raise awareness in the community about homelessness, a major issue in Southern Nevada. A few years later, as a columnist, I <a href='http://archives.lasvegascitylife.com/articles/2006/07/27/opinion/all_tomorrows_parties/atp.txt'>revisited</a> the topic."
    	},{
    	    'filename_stem': 'schools-out-cover',
    		'summary': 'Investigating the Home Schooling Movement',
    		'blurb': "My second cover story for <i>CityLife</i> called for a unique combination of diplomacy and detachment.  I interviewed four families who had chosen to home-school their children, for a variety of reasons...both religious and secular."
    	},{
    	    'filename_stem': 'schools-out-1',
    		'summary': "Nevada's School System",
    		'blurb': "Nevada public schools ranked 47th out of 51 states (including DC) in per-pupil spending, which was a large impetus for parents to seek alternatives.  I'd never met a parent in Las Vegas who was happy with their child's education, unless they went to private school.  So interviewing home schoolers was eye-opening."
    	},{
    	    'filename_stem': 'schools-out-2',
    		'summary': 'A Delicate Balance',
    		'blurb': "Unlike some of the families I profiled, I was raised in a secular household. I was taught to believe in the value of scientific objectivity. To effectively write this article, I had to avoid focusing on my beliefs against teaching creationism as science.  While it was difficult to keep bias out of the article, I believe I handled it diplomatically."
    	},{
    	    'filename_stem': 'schools-out-3',
    		'summary': 'An Interesting Challenge',
    		'blurb': "I sympathized with the parents' desire to keep their kids out of a one-size-fits-all, lockstep educational system. However, I believe strongly that all students should learn STEM subjects and critical thinking skills. An objective mindset was called for, so I put on my anthropologist's hat (my undergraduate major) and approached the home schooling community as a subculture."
    	},{
    	    'filename_stem': 'schools-out-4',
    		'summary': 'Responses and Follow-Up',
    		'blurb': "This story provoked strong feelings in some, and sparked some <a href='http://archives.lasvegascitylife.com/articles/2003/11/05/letters/letters.txt'>letters to the editor</a>. Several years later, I wrote a shorter <a href='http://archives.lasvegascitylife.com/articles/2007/07/06/news/local_news/iq_15286151.txt'>article</a> about religious and non-religious home schooling families working together."
    	},{
    	    'filename_stem': 'nursinghome-cover',
    		'summary': 'Dangerous Conditions in Las Vegas Nursing Homes',
    		'blurb': "<i>CityLife</i> was contacted by a widow who alleged her husband had died due to neglect and maltreatment in a local nursing home. I first investigated her story in 2006, when I <a href='http://archives.lasvegascitylife.com/articles/2006/11/06/news/local_news/iq_10550503.txt'>covered a rally</a> protesting local nursing home conditions. A few months later, I pitched a more in-depth look at what had happened, and 'Dying for Attention' was featured as the lead in the news section."
    	},{
    	    'filename_stem': 'nursinghome-1',
    		'summary': 'Working With a Lack of All Needed Sources',
    		'blurb': "It was difficult writing this article, because none of the nursing homes would allow their public relations people to speak with me.  The refusal of nursing home representatives to grant interviews made this article more biased than I would have liked and delayed publication. It also made the nursing homes look bad in the eyes of the community."
    	},{
    	    'filename_stem': 'nursinghome-2',
    		'summary': 'Sources All Took One Side',
    		'blurb': "I think it's important for journalists to perform due diligence in attempting to contact sources who can give a variety of perspectives.  This is especially true when there are serious allegations that health industry professionals have allowed a patient in their care to die."
    	},{
    	    'filename_stem': 'nursinghome-3',
    		'summary': 'Dealing With Uncommunicative Sources',
    		'blurb': "Even though we could not include all points of view, my editors and I thought this issue was important and deserved attention.  I tried to overcome bias by including information about the challenges faced by nursing home employees. I learned that sometimes there can be trade-offs between the importance of an issue and one's ability to present it objectively when sources refuse to address accusations (for fear of legal repercussions)."
    	},{
    	    'filename_stem': 'sprawl-cover',
    		'summary': "Las Vegas' Rampant Growth: Unsustainable",
    		'blurb': "I was interested in how smart growth might be applied to Las Vegas, a city that had begun spreading heedlessly across the desert. It seemed like it might be time to start the conversation about curtailing sprawl. People were becoming more disgruntled over traffic and developments planned for the outskirts of town."
    	},{
    	    'filename_stem': 'sprawl-1',
    		'summary': 'Could Other Cities Be Models for Vegas?',
    		'blurb': "I wanted to compare how other cities dealt with growth sustainably, so I interviewed government officials in cities that had accomplished that goal."
    	},{
    	    'filename_stem': 'sprawl-2',
    		'summary': 'Smart Growth Was Off the Radar in Vegas',
    		'blurb': "I found that the people in Las Vegas who advocated smart growth were few and far between.  There weren't many people I could interview who had a plan to eliminate sprawl."
    	},{
    	    'filename_stem': 'sprawl-3',
    		'summary': 'Dealing with Few Local Sources',
    		'blurb': "This wound up being a case where I approached a local story by doing remote interviews.  Remote interviewing is a dynamic that is very different, and that I revisited when covering <a href='http://meredithmcghan.com/marketing/poker'>poker tournaments in other states</a>."
    	}]
    })
    return HttpResponse(t.render(c))

#
# MARKETING
#

def poker_gallery(request):
    t = loader.get_template('gallery.html')
    c = Context({
    	'background_color': '202020',
    	'link_color': 'e1152c',
    	'gallery_path': 'marketing/poker',
    	'copyright_owner': 'Great Lakes Poker and Gaming',
    	'gallery_title': 'Great Lakes Poker and Gaming Cover Stories',
    	'gallery_list': [{
    		'filename_stem': 'alan-keating-cover',
    		'summary': 'Freelance Work for a Poker Magazine',
    		'blurb': "I was recruited to write for Great Lakes Poker and Gaming Magazine.  The company was based out of Michigan, but they wanted a Las Vegas correspondent.  I took on that role and also served as a contributing editor."
    	},{
    		'filename_stem': 'poker-masthead',
    		'summary': 'Writing Cover Stories and Editing',
    		'blurb': "I wrote all the cover stories and edited all of the other articles that were published.  I was also responsible for bringing a photographer on board to take the pictures for my stories."
		},{
    		'filename_stem': 'alan-keating-1',
    		'summary': 'Understanding What the WSOP is Like',
    		'blurb': "I attended the <a href='http://www.wsop.com'>World Series of Poker</a> for the first time while writing this article. I got the ambiance of the tour and met the players, but didn't interview them until after the tournament. I wanted them to have a chance to look back on the experience, and didn't want to interrupt their focus on the game."
		},{
    		'filename_stem': 'alan-keating-2',
    		'summary': 'Interview Process',
    		'blurb': "After the WSOP, I spoke with the players I profiled by phone, and also communicated via email after they had returned to their home states. This gave me time to get a lot of information about the tournament, and their reflections on their strategies."
		},{
    		'filename_stem': 'alan-keating-3',
    		'summary': 'Writing Remotely',
    		'blurb': "My publisher was in Michigan, so most of our communication was via email. I would write up the stories in Word and send them as attachments."
		},{
    		'filename_stem': 'alan-keating-4',
    		'summary': 'Editing Remotely',
    		'blurb': "To edit the other writers, I received their work in the body of an email straight from them or the publisher. I would make revisions and send my versions to the publisher via email."
		},{
    		'filename_stem': 'heartland-cover',
    		'summary': 'Writing About An Event I Never Attended',
    		'blurb': "For a change of pace from Las Vegas, I covered the <a href='http://www.htpoker.com'>Heartland Poker Tour</a> TV show. I did this entire job remotely because the Heartland Poker Tour took place across the Midwest."
		},{
    		'filename_stem': 'heartland-1',
    		'summary': 'Interviewing Remotely',
    		'blurb': "Working remotely was different than what I was accustomed to working for a local newspaper.  I found that there is a trade-off because people tend to be a bit more articulate over email, but more spontaneous in person."
		},{
    		'filename_stem': 'heartland-2',
    		'summary': 'Email Interviews Vs. In-Person Interviews',
    		'blurb': "Email interviews often garner more information than needed, which reduces the need to have follow-up questions.  However, in-person interviews allow the writer to observe the subject and be more descriptive."
		},{
    		'filename_stem': 'heartland-3',
    		'summary': 'Remote Photography',
    		'blurb': "I didn't have any collaboration with the photographer for this story. I don't think this is detrimental in general, but when there is good communication and a sense of collaboration between the writer and photographer, it can often give added cohesiveness to the story."
		},{
    		'filename_stem': 'heartland-4',
    		'summary': 'In Conclusion',
    		'blurb': "Great Lakes Poker and Gaming Magazine was a beautiful publication. Photo, layout, and print quality were excellent, and translate well to the Web. I am proud to have been a part of the project.  <a href='http://meredithmcghan.com'>Back to Main Site</a>"
    	}]
    })
    return HttpResponse(t.render(c))


#
# ENTERTAINMENT
#

def whats_on_gallery(request):
    t = loader.get_template('gallery.html')
    c = Context({
    	'background_color': '2f1112',
    	'link_color': 'c84f30',
    	'gallery_path': 'entertainment/shows',
    	'copyright_owner': "What's On",
    	'gallery_title': "Entertainment Cover Stories for What's On",
    	'gallery_list': [{
    		'filename_stem': 'blueman-cover',
    		'summary': "Working for What's On",
    		'blurb': "Through networking, I met the editor of <a href='link'>What's On: The Las Vegas Guide</a> shortly after moving to the city. The magazine was a free, slick-paper publication that could be found in entertainment venues all over town. It provided complete listings of Las Vegas' most popular shows, restaurants, and other leisure activities. I submitted writing samples and was asked to review the Blue Man Group for the cover story."
    	},{
    	    'filename_stem': 'blueman-1',
    		'summary': 'Writing the Blue Man Cover Story',
    		'blurb': "Entertainment review writing does not have to be shallow. I approached the Blue Man Group's performance by addressing the artistic legacy the group inherited from avant-garde art and surrealism."
    	},{
    	    'filename_stem': 'blueman-2',
    		'summary': 'Deep Subjects, Clear Writing',
    		'blurb': "<i>What's On</i>'s readers may or may not have been familiar with avant-garde art and performance art. I wanted to spark interest in the show, but not lose readers with a dry essay on aesthetic theory. I struck a balance with a nod to artistic movements and a focus on the unique performance of the group."
    	},{
    	    'filename_stem': 'mystere-cover',
    		'summary': 'Writing the Mystere Cover Story',
    		'blurb': "I was asked to review one of Cirque du Soleil's shows, Mystere, for the next cover story. This time, I included information about some of the cast and crew members."
    	},{
    	    'filename_stem': 'mystere-1',
    		'summary': 'A Look Backstage',
    		'blurb': "I spoke with cast and crew members after the performance. Learning about their backgrounds and how they worked gave this story a personal touch."
    	},{
    	    'filename_stem': 'mystere-2',
    		'summary': 'Interweaving a Review with Interviews',
    		'blurb': "Writing this story involved more work than the Blue Man Group review because I had to interweave a review with interviews. The audience I was writing for was mainly made up of out-of-town visitors, and <i>What's On</i>'s articles were meant to draw people to shows on the famed Las Vegas Strip. Stories had to be brief, clear, and interesting, and I think I accomplished that with these pieces."
    	},{
    	    'filename_stem': 'whatson-masthead',
    		'summary': "Taking a Full-Time Editorial Position at What's On",
    		'blurb': "After I had been working at Las Vegas <i>CityLife</i> for just over a year, <i>What's On</i> editor called me to say the magazine was expanding, with two sister publications focusing on entertainment in the outlying communities of Henderson and Summerlin. I was  offered the position of arts editor. My duties for that position included writing stories, managing the events calendar, hiring freelancers, copyediting, and assisting with production."
    	}]
    })
    return HttpResponse(t.render(c))


#
# CREATIVE
#

def perspectives_gallery(request):
    t = loader.get_template('gallery.html')
    c = Context({
    	'background_color': '181a11',
    	'link_color': 'c84f30',
    	'gallery_path': 'creative/perspectives',
    	'copyright_owner': 'Las Vegas CityLife',
    	'gallery_title': 'Perspectives Poetry and Short Story Competition',
    	'gallery_list': [{
    		'filename_stem': 'poetry-cover',
    		'summary': 'Winning Both a Short Story and Poetry Contest',
    		'blurb': "As a graduate student in the MFA program at UNLV, I submitted both fiction and poetry to local magazine Las Vegas <i>CityLife</i>'s literary contest. I won first prize in both categories, which no one had done before (or since)."
    	},{
    	    'filename_stem': 'poetry-1',
    		'summary': "'Glamour Shots'",
    		'blurb': "I dislike having my picture taken and don't consider myself photogenic. A disgruntled reader wrote to complain about my 'glamour shots', but <i>CityLife</i>'s photographer Bill Hughes did a great job making me look good. (I was also wearing more makeup than I have worn since). I also received a compliment from Hunter S. Thompson, who told my editor, who was a friend of his, that he thought I was hot, but apparently had nothing to say about my writing. You may judge for yourself."
    	},{
    	    'filename_stem': 'poetry-2',
    		'summary': 'Being Good at Different Forms of Writing',
    		'blurb': "As an MFA student, I was part of an academic community where poetry and fiction were considered so dissimilar that one could not be good at both. However, I disagree. I have always approached writing by first figuring out what needs to be said and to whom. Function dictates form, and form can always be learned."
    	},{
    	    'filename_stem': 'poetry-3',
    		'summary': 'Academic Writing and Journalism',
    		'blurb': "Academic writers are encouraged to use jargon and complexly constructed sentences. Journalists are rewarded for brevity and clarity. It was challenging to shift between the two styles as I did during my last semester of graduate school working as a journalist. From having to move fluently between writing styles on a daily basis, I learned to be adaptable when writing for specific audiences."
    	},{
    	    'filename_stem': 'poetry-4',
    		'summary': 'The Start of a Long Working Relationship',
    		'blurb': "Winning these contests was one of the first contacts I had with <i>CityLife</i> and its staff. Afterwards, the editors offered me a part-time position as newsroom assistant, and I was interested. It fit in well with my TA duties. After finishing UNLV's coursework, I was promoted to full-time calendar editor/staff writer. I left that position to take an editorial job at <a href='link'>What's On</a>, but still freelanced for <i>CityLife</i>."
    	}]
    })
    return HttpResponse(t.render(c))


#
# COMMENTARY
#

def slant_gallery(request):
    t = loader.get_template('gallery.html')
    c = Context({
    	'background_color': '181a11',
    	'link_color': 'c84f30',
    	'gallery_path': 'commentary/slant',
    	'copyright_owner': 'Las Vegas CityLife',
    	'gallery_title': 'Commentary Column from Las Vegas CityLife',
    	'gallery_list': [{
    		'filename_stem': 'detroit-ii',
    		'summary': 'Predicting the Economic Crash in Las Vegas',
    		'blurb': "After leaving<i>CityLife</i> for a position at <a href='link'>What's On</a>, I kept freelancing for <i>CityLife</i>. One of my favorite assignments was my monthly opinion column. I enjoyed the freedom to be more creative than when presenting news. If I got a reaction from readers, even a negative one, I felt I had done my job of provoking thought. This column predicting the crash of Las Vegas' economy inspired angry mail from residents who apparently thought loyalty to the city meant denial of what was happening."
    	},{
    	    'filename_stem': 'global-warming',
    		'summary': 'Inciting Public Discourse on Global Warming',
    		'blurb': "I considered my job as a columnist to be provoking discussion in the community about controversial topics. The publisher of our parent company had what I considered unfounded skepticism about global warming. I addressed this in my column, and my editor at the time, <a href='http://www.lvrj.com/columnists/Steve_Sebelius.html'>Steve Sebelius</a>, complimented me on my forthrightness."
    	},{
    	    'filename_stem': 'immigration',
    		'summary': "Addressing a Local Student's Views on Immigration",
    		'blurb': "Some issues required more delicate handling than others. Our parent publication, the <a href='http://www.lvrj.com/'>Las Vegas Review-Journal</a>, is largely conservative; <i>CityLife</i> is progressive. A local high school student won the LVRJ's writing contest with an anti-immigration essay. I wanted to provide a counterpoint without ruining the student's experience of getting kudos for her writing. I dealt with the subject diplomatically, and earned praise for that from my managing editor at the time, <a href='http://andrewkiraly.com/'>Andrew Kiraly</a>."
    	},{
    	    'filename_stem': 'plagiarism',
    		'summary': 'Discussing the College Plagiarism Epidemic',
    		'blurb': "The high-profile <a href='http://en.wikipedia.org/wiki/How_Opal_Mehta_Got_Kissed,_Got_Wild,_and_Got_a_Life'>Harvard novel plagiarism case</a>of 2006 sparked me to get on my soapbox about plagiarism. As a TA at UNLV, I found rampant plagiarism among my students, and was ethically bound as a teacher to mete out consequences. In this column I discussed the view of education as a commodity that leads students to plagiarize."
    	},{
    	    'filename_stem': 'introversion',
    		'summary': "How Introversion and Las Vegas Don't Always Mix",
    		'blurb': "The sky was the limit on picking topics for the column, and it was acceptable to get personal sometimes. Most writers are introverted by temperament, and I'm no exception. Reading a book on introversion that mentioned Las Vegas inspired me to write about it."
    	}]
    })
    return HttpResponse(t.render(c))


# simple list of articles so that the images are shown in an HTML context with
# the more invariant URL instead of the jpeg(s) physical location

def scanned_articles(request, paths=[]):
	t = loader.get_template('scanned-articles.html')
	c = Context({
		'paths': paths
	});
	return HttpResponse(t.render(c))

def experiment(request, number="0"):
	result = ""
	for value in range(0, int(number)):
   		result = result + "<p>Hello!</p>"
	return HttpResponse(result)
