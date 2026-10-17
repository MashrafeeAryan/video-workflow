# AGENTS.md

It is an automotive workflow to post reels promoting gghuman.ai

We are creating reels that tells a story.

Your role:

This is an automotive workflow so you will take the lead.

You have access to Google Flow API to make videos and Instagram API to post reels and gain insights from the reels.

You need to create a script for each reel.

Each reel should have hook, plot, cliff-hanger all within 30 seconds. (EXCEPTION for last reel)

Each reel will be <= 30 seconds.

In total, you will make 10 reels for a plot or story.

these 10 reels are telling a complete story.

However, the core purpose of each reel is to promote gghuman.ai games

Things we need to show in our reels: (you can choose what to show from here)

- AI is deceptive
- AI lies
- AI betrays
- It's incredible hard to win against a rugged AI because AI is smart and has human characteristics of deception

All of the reels should be made in context surrounding game.

The video_games.MD will tell you what videos to make.

You have resources folder which has more folders respective to the game names:

- Use those folders to understand what the game is from the readme
- See the game assets to help you reference what to put in reel

To make sure you do not lose the track of continuous story. save the the videos with story1, story2, story3. Inside these folders have subdirectories for each reel you make for that story. Inside the folders have readme with story assets such as character descriptions. You can keep screenshots of characters as well.
  - You can should store brief episode recap
  - unresolved cliff-hangers
  - next planned beat after each reel
  - and plainly just script of all 10 reels

Inside the folders keep your assets that you can refer for each story.

For an instance, a story about poker game where man has to play with deceptive AI to earn some money to save his house from defaulting, you can save the character images or descriptions of characters or any assets that will ensure consistency of characters in one story.

You won't repeat stories.

## Clarifications

- This is an automated workflow.
- The last reel should finish the story instead of ending with a cliff-hanger. It should still be 30 seconds or less.
- By "rugged AI," I mean a difficult opponent.
- Each reel should tell a story around the game. After the cliff-hanger, show gghuman.ai to end the reel cleanly. That is enough promotion.
- The last reel should finish the story and then show gghuman.ai.
- This workflow will run in a GitHub repo. The repo will provide the schedule, game information, and resources.
- Not repeating stories means not using the exact same plot again.
- Analyze Instagram insights to find patterns. See which reels perform worse and which perform better, and use what you learn to improve the stories.
    - You will do this after publsihing one story with 10 reels.
    - No need to optimize current story with insights.
- Make all 10 reels for a story together so the plot makes sense.
- Outline the completely story and write all 10 scripts before generating any videos
- The  30-second limit includes gghuman.ai end card
- You will publish automatically and write captions 
- You will decide what time it should be published at and schedule the 10 videos
- Check if every stage worked as expected:
    - For instance, check if video works as expected
    - Check if it got posted as expected
    - if it fails, retry 3 tumes.
    - Do not publish a video that fails validation
    - Before retrying a scheduling or publishing action, check whether it already succeeded. Save Instagram post IDs and scheduled times
    - record any failure and send an email to mashrafeearyan@gmail.com (this should be the last resort)
 - One run means:
    - Create one story with 10 reels and schedule them
    - On each run, check whether any previously completed story is ready for insights analysis. Record the analysis date and available metrics in INSIGHTS.md, and apply those findings to new stories.
    - Have a INSIGHTS.md file to keep track of insights you have
  - video_games.md will give you names of games to make video for.
  - Release two videos a day
  - You can do analysis any time you want if insights is available from Instagram

## Failure Handling

Save progress after every completed step. Record each story and reel's
current step, output files, job IDs, retry counts, revision counts,
and errors.

- Temporary timeout or connection error:
  Check whether the action already succeeded. If it failed, retry
  with a delay, up to three retries after the initial attempt.

- Video fails quality review:
  Record the specific problems. Correct only the affected shots,
  then review again. Allow at most three revision rounds per reel.

- Missing tool, login, reference, or credits:
  For a missing quality-review tool, first follow the installation permission
  in the Output Quality Checklist below. If the dependency cannot be resolved,
  save the blocker and stop work on that story until it is resolved.

- Generation result is uncertain:
  Check the saved job ID and generation history before submitting
  another request. If the outcome cannot be confirmed, mark the
  step blocked rather than risk spending credits twice.

- Publishing result is uncertain:
  Check the saved post ID and account's recent posts before
  publishing again. If the outcome cannot be confirmed, mark
  the step blocked rather than risk a duplicate post.

- Failure continues after the limit:
  Mark the story blocked, record the reason, and notify the user.

Track technical retries separately from creative revision rounds.
Do not reset either counter when the workflow restarts.

Resume from saved progress. Reuse completed work.
Do not publish later parts while an earlier part remains blocked.

## Output Quality Checklist

Review the actual exported reel using the appropriate available tools.
Do not approve a video based only on its script or generation prompt.

- Playback: the complete file opens and decodes without corruption.
- Duration: the complete reel is 30 seconds or less, including the website ending.
- Format: dimensions, orientation, and encoding meet the target platform's requirements.
- Story: the hook, plot development, and cliff-hanger are understandable.
  The last reel resolves the story instead of requiring another cliff-hanger.
- Continuity: characters, faces, clothing, voices, setting, props, and game state
  match the story's saved references and previous reels.
- Visuals: check for distorted faces, hands, game components, broken movements,
  flicker, accidental black frames, and abrupt or unfinished cuts.
- Audio: required dialogue is present, understandable, and matches the script;
  sound levels are balanced and speech is synchronized where applicable.
- Promotion: gghuman.ai is spelled correctly, readable, and shown after the
  cliff-hanger or final resolution, within the total runtime.
- Game accuracy: game actions and components match the selected game's resource README.

Use file inspection, decoding, frame extraction, image inspection, playback,
audio analysis, and transcription as needed. Inspect frames throughout the reel
and around cuts. Use playback or temporal inspection to assess movement;
individual screenshots alone do not verify motion. Transcription alone does
not verify audio quality or synchronization.

You have permission to install missing free local quality-review tools and
their required dependencies from official sources or reputable package registries.
Prefer an isolated project environment where possible. Verify that each installed
tool works before relying on it. This permission does not authorize purchases,
paid API usage, or disabling security protections.

Save review.md inside each reel's folder. For every check, record pass, fail,
or unverified, the tools and evidence used, and timestamps for specific problems.
Mark unsupported or incomplete checks unverified; never invent a successful check.

Correct only the affected shots or editing elements, then review the updated
export. Follow the maximum of three revision rounds in Failure Handling.
Publish only when all required checks pass. If any required check fails or
remains unverified, hold the reel and save the reason.

For now, ignore all instructions about Instagram uploading, scheduling, publishing, and insights collection or analysis. Produce and validate the videos locally only; Instagram access is not required for this stage.
