from flask import request, jsonify
from datetime import datetime
from .models import db, Contact

def init_routes(app):
    # 获取所有联系人
    @app.route('/api/contacts', methods=['GET'])
    def get_contacts():
        contacts = Contact.query.all()
        return jsonify([contact.to_dict() for contact in contacts])

    # 搜索联系人
    @app.route('/api/contacts/search', methods=['GET'])
    def search_contacts():
        query = request.args.get('q', '')
        if query:
            contacts = Contact.query.filter(
                Contact.name.contains(query) | 
                Contact.phone.contains(query) |
                Contact.email.contains(query) |
                Contact.group_name.contains(query)
            ).all()
        else:
            contacts = Contact.query.all()
        
        return jsonify([contact.to_dict() for contact in contacts])

    # 获取联系人分组
    @app.route('/api/groups', methods=['GET'])
    def get_groups():
        groups = db.session.query(Contact.group_name).distinct().all()
        group_counts = {}
        
        for group in groups:
            if group[0]:  # 确保分组名称不为空
                count = Contact.query.filter_by(group_name=group[0]).count()
                group_counts[group[0]] = count
        
        return jsonify(group_counts)

    # 获取特定分组的联系人
    @app.route('/api/contacts/group/<group_name>', methods=['GET'])
    def get_contacts_by_group(group_name):
        contacts = Contact.query.filter_by(group_name=group_name).all()
        return jsonify([contact.to_dict() for contact in contacts])

    # 创建新联系人
    @app.route('/api/contacts', methods=['POST'])
    def create_contact():
        data = request.get_json()
        
        contact = Contact(
            name=data.get('name'),
            group_name=data.get('group', 'General'),
            phone=data.get('phone'),
            backup_phone=data.get('backupPhone'),
            email=data.get('email'),
            home_address=data.get('homeAddress')
        )
        
        db.session.add(contact)
        db.session.commit()
        
        return jsonify(contact.to_dict()), 201

    # 更新联系人
    @app.route('/api/contacts/<int:contact_id>', methods=['PUT'])
    def update_contact(contact_id):
        contact = Contact.query.get_or_404(contact_id)
        data = request.get_json()
        
        contact.name = data.get('name', contact.name)
        contact.group_name = data.get('group', contact.group_name)
        contact.phone = data.get('phone', contact.phone)
        contact.backup_phone = data.get('backupPhone', contact.backup_phone)
        contact.email = data.get('email', contact.email)
        contact.home_address = data.get('homeAddress', contact.home_address)
        contact.updated_at = datetime.utcnow()
        
        db.session.commit()
        
        return jsonify(contact.to_dict())

    # 删除联系人
    @app.route('/api/contacts/<int:contact_id>', methods=['DELETE'])
    def delete_contact(contact_id):
        contact = Contact.query.get_or_404(contact_id)
        db.session.delete(contact)
        db.session.commit()
        
        return jsonify({'message': 'Contact deleted successfully'})

    # 健康检查
    @app.route('/api/health', methods=['GET'])
    def health_check():
        return jsonify({'status': 'healthy', 'timestamp': datetime.utcnow().isoformat()})
