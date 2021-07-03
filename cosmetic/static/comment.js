function warnEmpty(){
		alert("Enter a Input");
	}

function dateToString(date) {
		const dateString = date.toISOString();
		const dateToString = dateString.substring(0,10)+ " " + dateString.substring(11,19);
		return dateToString;
	}

function submitComment(){
		const newcommentEL = document.getElementById("new-comment");
		const newcomment = newcommentEL.value.trim();

		if(newcomment)
		{		
			const dateEL = document.createElement('div');
			dateEL.classList.add("newcomment-date");
			const dateString = dateToString(new Date());
			dateEL.innerText = dateString;
		
			const contentEL = document.createElement('div');
			contentEL.classList.add('newcomment-content');
			contentEL.innerText = "이성규 : "+newcomment;
			
			const commentEL = document.createElement('div');
			commentEL.classList.add('comment-row');
			commentEL.appendChild(dateEL);
			commentEL.appendChild(contentEL);
		
			document.getElementById('comments').appendChild(commentEL);
			newcommentEL.value="";
		
			const countEL = document.getElementById('comments-count');
			const count = countEL.innerText;
			countEL.innerText = parseInt(count) + 1;
		}
		else warnEmpty();	
	}