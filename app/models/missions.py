from app import db
from flask import jsonify

class Missions(db.Model):
    __tablename__ = 'Missao'
    __table_args__ = {'sqlite_autoincrement': True} 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    launch_date = db.Column(db.DateTime)
    destination = db.Column(db.String(255))
    status = db.Column(db.String(50))
    tripulation = db.Column(db.String(255))
    util_charge = db.Column(db.String(255))
    duration = db.Column(db.Integer)
    cost = db.Column(db.Float)
    status_descr = db.Column(db.String(255))

    def __init__(self, name, launch_date, destination, 
                 status, tripulation, util_charge, 
                 duration, cost, status_descr):
        self.name = name
        self.launch_date = launch_date
        self.destination = destination
        self.status = status
        self.tripulation = tripulation
        self.util_charge = util_charge
        self.duration = duration
        self.cost = cost
        self.status_descr = status_descr

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'launch_date': self.launch_date.isoformat() if self.launch_date else None,
            'destination': self.destination,
            'status': self.status,
            'tripulation': self.tripulation,
            'util_charge': self.util_charge,
            'duration': self.duration,
            'cost': self.cost,
            'status_descr': self.status_descr
        }
     
    def save_mission(self, name, launch_date, destination, 
                 status, tripulation, util_charge, 
                 duration, cost, status_descr):
        try:
            add_banco = Missions(name, launch_date, destination, 
                 status, tripulation, util_charge, 
                 duration, cost, status_descr)
            print(add_banco)
            db.session.add(add_banco) 
            db.session.commit()
        except Exception as e:
            print(e)

    def view_missions(self):
        missions_json = []
        missions = db.session.query(Missions).order_by(Missions.launch_date.desc()).all()
        for mission in missions:
            missions_json.append(mission.to_dict())
        return missions_json


    def view_mission(self, id):
        try:
            mission = db.session.query(Missions).filter(Missions.id==id).first()
            if mission:
                return mission.to_dict()
            else:
                return {'message': 'Mission not found'}, 404        
        except Exception as e:
            print(e)
            return {'message': e}, 500  


    
    def delete_mission(self, id):
        try:
            mission = db.session.query(Missions).filter(Missions.id==id).first()
            if mission:
                db.session.delete(mission)
                db.session.commit()       
                return {'message': 'Mission deleted'}, 200 
            else:
                return {'message': 'Mission not found'}, 404  
        except Exception as e:
            print(e)
            return {'message': e}, 500  


    def update_mission(self, id, name, launch_date, destination, 
                 status, tripulation, util_charge, 
                 duration, cost, status_descr):
        try:
            mission = db.session.query(Missions).filter(Missions.id==id).first()
            if mission:
                mission.name = name
                mission.launch_date = launch_date
                mission.destination = destination
                mission.status = status
                mission.tripulation = tripulation
                mission.util_charge = util_charge
                mission.duration = duration
                mission.cost = cost
                mission.status_descr = status_descr
                db.session.commit()
                return {'message': 'Mission updated'}, 200
            else:
                return {'message': 'Mission not found'}, 404  
        except Exception as e:
            print(e)
            return {'message': e}, 500  



    def view_mission_per_date(self, date_start, date_end):
        try:
            missions_json = []
            missions = db.session.query(Missions).filter(Missions.launch_date>=date_start).filter(Missions.launch_date<=date_end).all()
            if missions:
                for mission in missions:
                    missions_json.append(mission.to_dict())
                return missions_json
            else:
                return {'message': 'Mission not found'}, 404
        except Exception as e:
            print(e)
            return {'message': e}, 500  
