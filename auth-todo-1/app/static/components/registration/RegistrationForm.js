var RegistrationForm = React.createClass({
		getInitialState:function(){
			return ({
				username: "",
				password:"",
				confirmPassword:""
			});
		},
		toggleUsername:function(e){
				this.setState({
					username:e.target.value
				});
		},
		togglePassword:function(e){
				this.setState({
					password:e.target.value
				});
		},
		toggleConfirmPassword:function(e){
				this.setState({
					confirmPassword:e.target.value
				});
		},
		register:function(e){
			console.log(e);
			e.preventDefault();
			
			if(this.state.password === this.state.confirmPassword){
				
				axios.post('/register',{
					username:this.state.username,
					password:this.state.password,
					confirmPassword:this.state.confirmPassword

				})
				.then(function (response) {
				    console.log(response);
				  })
				  .catch(function (error) {
				    console.log(error);
				  });

			}
			else{
				alert("Passwords are not in alignment");
			}
		},

		render:function(){
			return(
				<form onSubmit={this.register}>
					<input type="text" value={this.state.username} onChange={this.toggleUsername}/>
					<input type="password" value={this.state.password} onChange={this.togglePassword}/>
					<input type="password" value={this.state.confirmPassword} onChange={this.toggleConfirmPassword}/>
					<input type="hidden" name="csrf_token" value="{{ csrf_token() }}"/>
					<input type="submit" value="Register"/>
				</form>
				)
		}
});