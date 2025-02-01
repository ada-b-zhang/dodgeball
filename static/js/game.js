class Game {
    constructor() {
        this.canvas = document.getElementById('gameCanvas');
        this.ctx = this.canvas.getContext('2d');
        this.width = 800;
        this.height = 600;
        this.player = {
            x: 400,
            y: 500,
            width: 25,
            height: 50,
            speed: 5,
            color: '#4287f5'
        };
        this.enemies = [];
        this.playerBalls = [];
        this.enemyBalls = [];
        this.foods = [];
        this.hp = 3;
        this.level = 1;
        this.gameStarted = false;
        this.keys = {};

        this.setupEventListeners();
        this.setupModals();
    }

    setupEventListeners() {
        document.addEventListener('keydown', (e) => {
            this.keys[e.key] = true;
            if (e.key === 'd' || e.key === 'D') {
                this.throwBall();
            }
        });

        document.addEventListener('keyup', (e) => {
            this.keys[e.key] = false;
        });

        document.getElementById('startButton').addEventListener('click', () => {
            if (!this.gameStarted) {
                this.startGame();
            }
        });
        document.getElementById('restartButton').addEventListener('click', () => {
            $('#gameOverModal').modal('hide');
            this.resetGame();
            this.startGame();
        });
    }

    setupModals() {
        this.gameOverModal = new bootstrap.Modal(document.getElementById('gameOverModal'), {
            keyboard: false,
            backdrop: 'static'
        });
    }

    startGame() {
        this.gameStarted = true;
        this.spawnEnemies();
        this.gameLoop();
        document.getElementById('startButton').style.display = 'none';
    }

    spawnEnemies() {
        this.enemies = [];
        for (let i = 0; i < this.level * 5; i++) {
            this.enemies.push({
                x: Math.random() * (this.width - 50) + 25,
                y: Math.random() * 150 + 100,
                width: 25,
                height: 50,
                color: '#f5424e',
                speedX: this.level,
                speedY: this.level
            });
        }
    }

    throwBall() {
        if (this.gameStarted) {
            const ball = {
                x: this.player.x,
                y: this.player.y,
                radius: 10,
                speedY: -10,
                speedX: this.keys['ArrowLeft'] ? -5 : this.keys['ArrowRight'] ? 5 : 0,
                color: '#42f54e'
            };
            this.playerBalls.push(ball);
        }
    }

    update() {
        // Player movement
        if (this.keys['ArrowLeft']) {
            this.player.x = Math.max(this.player.x - this.player.speed, this.player.width/2);
        }
        if (this.keys['ArrowRight']) {
            this.player.x = Math.min(this.player.x + this.player.speed, this.width - this.player.width/2);
        }

        // Update balls
        this.playerBalls.forEach((ball, index) => {
            ball.y += ball.speedY;
            ball.x += ball.speedX;

            // Remove balls that are off screen
            if (ball.y < 0) {
                this.playerBalls.splice(index, 1);
            }
        });

        // Enemy movement and ball throwing
        this.enemies.forEach(enemy => {
            enemy.x += (Math.random() - 0.5) * enemy.speedX;
            enemy.y += (Math.random() - 0.5) * enemy.speedY;

            // Keep enemies in bounds
            enemy.x = Math.max(Math.min(enemy.x, this.width - enemy.width/2), enemy.width/2);
            enemy.y = Math.max(Math.min(enemy.y, 325 - enemy.height/2), enemy.height/2);

            // Random enemy ball throwing
            if (Math.random() < 0.01) {
                this.enemyBalls.push({
                    x: enemy.x,
                    y: enemy.y,
                    radius: 10,
                    speedY: 3 + this.level/2,
                    speedX: (Math.random() - 0.5) * 3,
                    color: '#f542f2'
                });
            }
        });

        // Update enemy balls
        this.enemyBalls.forEach((ball, index) => {
            ball.y += ball.speedY;
            ball.x += ball.speedX;

            // Check collision with player
            const dx = ball.x - this.player.x;
            const dy = ball.y - this.player.y;
            if (Math.sqrt(dx*dx + dy*dy) < ball.radius + this.player.width/2) {
                this.hp--;
                this.enemyBalls.splice(index, 1);
                this.updateStats();
                if (this.hp <= 0) {
                    this.gameOver();
                }
            }

            // Remove balls that are off screen
            if (ball.y > this.height) {
                this.enemyBalls.splice(index, 1);
            }
        });

        // Check player ball collisions with enemies
        this.playerBalls.forEach((ball, ballIndex) => {
            this.enemies.forEach((enemy, enemyIndex) => {
                const dx = ball.x - enemy.x;
                const dy = ball.y - enemy.y;
                if (Math.sqrt(dx*dx + dy*dy) < ball.radius + enemy.width/2) {
                    this.enemies.splice(enemyIndex, 1);
                    this.playerBalls.splice(ballIndex, 1);

                    if (this.enemies.length === 0) {
                        this.nextLevel();
                    }
                }
            });
        });
    }

    draw() {
        // Clear canvas
        this.ctx.fillStyle = 'black';
        this.ctx.fillRect(0, 0, this.width, this.height);

        // Draw court line
        this.ctx.strokeStyle = 'darkred';
        this.ctx.lineWidth = 5;
        this.ctx.beginPath();
        this.ctx.moveTo(0, 325);
        this.ctx.lineTo(this.width, 325);
        this.ctx.stroke();

        // Draw player
        this.ctx.fillStyle = this.player.color;
        this.ctx.fillRect(
            this.player.x - this.player.width/2,
            this.player.y - this.player.height/2,
            this.player.width,
            this.player.height
        );

        // Draw enemies
        this.enemies.forEach(enemy => {
            this.ctx.fillStyle = enemy.color;
            this.ctx.fillRect(
                enemy.x - enemy.width/2,
                enemy.y - enemy.height/2,
                enemy.width,
                enemy.height
            );
        });

        // Draw player balls
        this.playerBalls.forEach(ball => {
            this.ctx.fillStyle = ball.color;
            this.ctx.beginPath();
            this.ctx.arc(ball.x, ball.y, ball.radius, 0, Math.PI * 2);
            this.ctx.fill();
        });

        // Draw enemy balls
        this.enemyBalls.forEach(ball => {
            this.ctx.fillStyle = ball.color;
            this.ctx.beginPath();
            this.ctx.arc(ball.x, ball.y, ball.radius, 0, Math.PI * 2);
            this.ctx.fill();
        });
    }

    updateStats() {
        document.getElementById('hp').textContent = this.hp;
        document.getElementById('level').textContent = this.level;
    }

    nextLevel() {
        this.level++;
        this.updateStats();
        this.spawnEnemies();
    }

    resetGame() {
        this.hp = 3;
        this.level = 1;
        this.updateStats();
        this.enemies = [];
        this.playerBalls = [];
        this.enemyBalls = [];
    }


    gameOver() {
        this.gameStarted = false;
        document.getElementById('finalLevel').textContent = this.level;
        this.gameOverModal.show();
        document.getElementById('startButton').style.display = 'block';
        this.resetGame();
    }

    gameLoop() {
        if (this.gameStarted) {
            this.update();
            this.draw();
            requestAnimationFrame(() => this.gameLoop());
        }
    }
}

// Start the game when the page loads
window.addEventListener('load', () => {
    const game = new Game();
});