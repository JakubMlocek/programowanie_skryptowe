exports.Operation = class {
    constructor(x = 5 ,y = 5) {
        this.x = x;
        this.y = y
    }

    sum() {
        return (this.x + this.y);
    }
}

