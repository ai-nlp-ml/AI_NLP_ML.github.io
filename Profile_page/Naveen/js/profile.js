$( document ).on( 'click', '#home_btn', function(evt) {
		$('#home_btn').css("background", "#ff0000");
		$("#home_content").css("display", "block");
		$("#education_content").css("display", "none");
		$("#education_btn").css("background", "#4E9CAF");
		$("#research_content").css("display", "none");
		$("#research_btn").css("background", "#4E9CAF");
		$("#industry_experience_content").css("display", "none");
		$("#IndustryExperience_btn").css("background", "#4E9CAF");
	});
	/*$('#sl_acc_rpt_btn').click(function() {*/
	$( document ).on( 'click', '#education_btn', function(evt) {
		$('#education_btn').css("background", "#ff0000");
		$("#home_btn").css("background", "#4E9CAF");
		$("#home_content").css("display", "none");
		$("#education_content").css("display", "block");
		$("#research_content").css("display", "none");
		$("#research_btn").css("background", "#4E9CAF");
		$("#industry_experience_content").css("display", "none");
		$("#IndustryExperience_btn").css("background", "#4E9CAF");
	});
	$( document ).on( 'click', '#research_btn', function(evt) {
		$('#research_btn').css("background", "#ff0000");
		$("#home_btn").css("background", "#4E9CAF");
		$("#home_content").css("display", "none");
		$("#education_content").css("display", "none");
		$("#education_btn").css("background", "#4E9CAF");
		$("#research_content").css("display", "block");
		$("#industry_experience_content").css("display", "none");
		$("#IndustryExperience_btn").css("background", "#4E9CAF");
	});
	$( document ).on( 'click', '#IndustryExperience_btn', function(evt) {
		$('#IndustryExperience_btn').css("background", "#ff0000");
		$("#home_btn").css("background", "#4E9CAF");
		$("#home_content").css("display", "none");
		$("#education_content").css("display", "none");
		$("#education_btn").css("background", "#4E9CAF");
		$("#research_content").css("display", "none");
		$("#research_btn").css("background", "#4E9CAF");
		$("#industry_experience_content").css("display", "block");

	});